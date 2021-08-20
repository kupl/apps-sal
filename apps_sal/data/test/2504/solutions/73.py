from scipy.sparse.csgraph import floyd_warshall
(N, M, L) = list(map(int, input().split()))
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
graph = floyd_warshall(graph)
another = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] <= L:
            another[i][j] = 1
another = floyd_warshall(another)
Q = int(input())
for _ in range(Q):
    (s, t) = [int(x) - 1 for x in input().split()]
    if another[s][t] == float('inf'):
        print(-1)
    else:
        print(int(another[s][t]) - 1)
