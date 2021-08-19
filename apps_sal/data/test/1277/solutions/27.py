from collections import deque
(n, u, v) = map(int, input().split())
u -= 1
v -= 1
edges = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)


def bfs(u):
    visited = [-1] * n
    Q = deque()
    visited[u] = 0
    Q.append(u)
    while Q:
        p = Q.popleft()
        for v in edges[p]:
            if visited[v] == -1:
                visited[v] = visited[p] + 1
                Q.append(v)
    return visited


tak_dist = bfs(u)
aok_dist = bfs(v)
ans = []
for i in range(n):
    if tak_dist[i] < aok_dist[i]:
        ans.append(aok_dist[i])
print(max(ans) - 1)
