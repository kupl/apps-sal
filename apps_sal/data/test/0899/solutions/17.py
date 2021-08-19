(N, M) = map(int, input().split())
graph = [[] for _ in range(N)]
cost = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    (a, b, c) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    cost[a - 1][b - 1] = c
    cost[b - 1][a - 1] = c


def dijkstra(S, N, cost):
    d = [float('inf')] * N
    used = [False] * N
    d[S] = 0
    while True:
        v = -1
        for i in range(N):
            if not used[i] and v == -1:
                v = i
            elif not used[i] and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True
        for j in range(N):
            d[j] = min(d[j], d[v] + cost[v][j])
    return d


dist = []
for s in range(N):
    dist.append(dijkstra(s, N, cost))
checked = [[False] * N for _ in range(N)]
ans = M
for s in range(N):
    for i in range(s, N):
        for j in graph[i]:
            if checked[i][j]:
                continue
            if dist[s][i] + cost[i][j] == dist[s][j]:
                ans -= 1
                checked[i][j] = True
                checked[j][i] = True
print(ans)
