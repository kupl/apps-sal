from collections import deque


def bfs(source, graph, mark, num, fcount):
    visited = [source]
    q = deque()
    mark[source] = True
    q.append(source)
    while q:
        u = q.popleft()
        for (v, c) in g[u]:
            if c == num and (not mark[v]):
                mark[v] = True
                visited.append(v)
                q.append(v)
    if len(visited) > 1:
        for u in visited:
            fcount[u] = len(visited)


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(0, n - 1)]
g = [[] for _ in range(0, n)]
cnt = [[0 for _ in range(0, n)] for _ in range(0, 2)]
for (u, v, c) in edges:
    g[u - 1].append((v - 1, c))
    g[v - 1].append((u - 1, c))
res = 0
for link in range(0, 2):
    mark = [False] * n
    for u in range(0, n):
        if not mark[u]:
            bfs(u, g, mark, link, cnt[link])
            res += cnt[link][u] * (cnt[link][u] - 1)
for i in range(0, n):
    if cnt[0][i] > 0 and cnt[1][i] > 1:
        res += (cnt[0][i] - 1) * (cnt[1][i] - 1)
print(int(res))
