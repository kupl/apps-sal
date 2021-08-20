from copy import deepcopy
(n, m) = map(int, input().split())
graph = [[10 ** 9 for _ in range(n)] for _ in range(n)]
edge = []
for _ in range(m):
    (a, b, c) = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
    edge.append((a, b))
for i in range(n):
    graph[i][i] = 0
distance = deepcopy(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
ans = 0
for (i, j) in edge:
    if distance[i][j] < graph[i][j]:
        ans += 1
print(ans)
