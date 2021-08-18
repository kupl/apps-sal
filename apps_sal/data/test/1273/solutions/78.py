from collections import deque
n = int(input())
tree = [[] for i in range(n + 1)]
edge = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    edge.append((a, b))
m = len(max(tree, key=len))
col = [0] * (n + 1)
col[1] = 'a'
Q = deque([1])
ans = {}
while Q:
    temp = Q.popleft()
    now = 1
    for n in tree[temp]:
        if col[n]:
            continue
        if now == col[temp]:
            now += 1
        col[n] = now
        ans[min(temp, n), max(temp, n)] = now
        now += 1
        Q.append(n)

print(m)
for a, b in edge:
    print(ans[(a, b)])
