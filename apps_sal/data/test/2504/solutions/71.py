import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
inf = float("inf")
N, M, L = map(int, input().split())
graph = np.zeros((N, N))
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1][B-1] = C
    graph[B-1][A-1] = C
shortest_paths = dijkstra(csr_matrix(graph), directed=False)
graph = np.full((N, N), inf)
for i in range(N):
    for j in range(N):
        if shortest_paths[i][j] <= L:
            graph[i][j] = 1

Q = int(input())
def int_(num_str):
    return int(num_str) - 1

costs = dijkstra(csr_matrix(graph), directed=False)
for _ in range(Q):
    s, t = map(int_, input().split())
    print(int(costs[s][t])-1 if costs[s][t] != inf else -1)
