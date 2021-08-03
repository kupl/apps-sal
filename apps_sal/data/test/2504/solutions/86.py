import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix


def f(): return map(int, input().split())


N, M, L = f()
G = [[0] * N for _ in [0] * N]
for _ in [0] * M:
    a, b, c = f()
    G[a - 1][b - 1] = c
    G[b - 1][a - 1] = c

csr = csr_matrix(G)

D = floyd_warshall(csr)
INF = float('inf')
G = [[INF] * N for _ in [0] * N]
for i in range(N):
    for j in range(N):
        if i != j and D[i][j] <= L:
            G[i][j] = 1
            G[j][i] = 1
csr = csr_matrix(G)
res = floyd_warshall(csr)
Q = int(input())
for _ in [0] * Q:
    s, t = f()
    r = res[s - 1][t - 1]
    print(int(r - 1) if r < INF else -1)
