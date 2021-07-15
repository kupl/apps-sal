from collections import deque, defaultdict
N = int(input())
d = defaultdict(list)
m = dict()
ls = []
for i in range(N-1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
    ls.append((a, b))

K = 0
for i in range(N):
    d[i+1].sort()
    K = max(K, len(d[i+1]))
print(K)

q = deque([])
q.append((1, 0))
visited = [0 for i in range(N+1)]
visited[1] = 1
while q:
    l, r = q.popleft()
    flag = 0
    cur = 1
    for i, x in enumerate(d[l], start=1):
        if visited[x] == 1:
            continue
        if flag == 0:
            if cur == r:
                q.append((x, cur+1))
                m[(l, x)] = cur+1
                m[(x, l)] = cur+1
                cur += 2
                visited[x] = 1
                flag = 1
                continue
            m[(l, x)] = cur
            m[(x, l)] = cur
            q.append((x, cur))
            cur += 1
            visited[x] = 1
        else:
            q.append((x, cur))
            m[(l, x)] = cur
            m[(x, l)] = cur
            cur += 1
            visited[x] = 1
for i in range(N-1):
    a, b = ls[i]
    print(m[(a, b)])
