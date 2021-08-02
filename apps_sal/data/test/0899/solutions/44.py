N, M = map(int, input().split())
INF = float('inf')
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
graph = [[INF if i != j else 0 for i in range(N)] for j in range(N)]
for i in range(M):
    a, b, c = edges[i]
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
ans = 0
for i in range(M):
    a, b, c = edges[i]
    if c != graph[a - 1][b - 1]:
        ans += 1
print(ans)
