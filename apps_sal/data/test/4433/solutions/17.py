from collections import deque
(n, m) = list(map(int, input().split()))
g = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
root = 0
for i in range(1, n + 1):
    if len(g[i]) > len(g[root]):
        root = i
visited = [False for i in range(n + 1)]
q = deque([root])
visited[root] = True
while len(q) > 0:
    u = q.popleft()
    for v in g[u]:
        if not visited[v]:
            q.append(v)
            print(u, v)
            visited[v] = True
