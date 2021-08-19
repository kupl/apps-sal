from collections import deque
(n, x, y) = map(int, input().split())
g = [[] for _ in range(n)]
g[0].append(1)
g[n - 1].append(n - 2)
g[x - 1].append(y - 1)
g[y - 1].append(x - 1)
for i in range(n - 2):
    g[i + 1].append(i)
    g[i + 1].append(i + 2)


def bfs(u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


ans_dist = [0 for i in range(n)]
for i in range(n):
    D = bfs(i)
    for d in D:
        ans_dist[d] += 1
for i in range(n - 1):
    print(ans_dist[i + 1] // 2)
