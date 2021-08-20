import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
(N, M, L) = list(map(int, input().split()))
G = np.full((N, N), np.inf)
np.fill_diagonal(G, 0)
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    G[a - 1][b - 1] = G[b - 1][a - 1] = c
D = floyd_warshall(G, directed=False)
G2 = np.full((N, N), np.inf)
np.fill_diagonal(G2, 0)
G2[D <= L] = 1
D2 = floyd_warshall(G2, directed=False)
Q = int(input())
for _ in range(Q):
    (a, b) = [int(x) - 1 for x in input().split()]
    if D2[a][b] == np.inf:
        print(-1)
    else:
        print(int(D2[a][b]) - 1)
