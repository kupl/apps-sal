from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

# neighborhood graph
nei_graph = [[0] * N for _ in range(N)]
for a, b, c in G:
    nei_graph[a - 1][b - 1] = c
    nei_graph[b - 1][a - 1] = c

# Warshall Floyd
nei_graph = floyd_warshall(nei_graph)

# 1 if distance is less than L
for i in range(N):
    for j in range(N):
        if nei_graph[i][j] <= L:
            nei_graph[i][j] = 1
        else:
            nei_graph[i][j] = 0

nei_graph = floyd_warshall(nei_graph)

for start, end in Query:
    if nei_graph[start - 1][end - 1] - 1 == float('inf'):
        print(-1)
    else:
        print(int(nei_graph[start - 1][end - 1] - 1))
