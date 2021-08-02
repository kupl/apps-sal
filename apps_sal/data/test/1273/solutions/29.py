from collections import deque, defaultdict
n = int(input())
data = [[] for _ in range(n)]
sides = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    data[a].append(b)
    data[b].append(a)
    sides.append((a, b))
I = defaultdict(lambda: 0)
cs = [0] * n
used = [0] * n
q = deque([0])
used[0] = 1
k = 0
while q:
    u = q.popleft()
    if k < len(data[u]):
        k = len(data[u])
    cur = 1
    for v in data[u]:
        if used[v]:
            continue
        if cur == cs[u]:
            cur += 1
        cs[v] = cur
        I[(u, v)] = cur
        I[(v, u)] = cur
        cur += 1
        used[v] = 1
        q.append(v)
print(k)
for i, j in sides:
    print(I[(i, j)])
