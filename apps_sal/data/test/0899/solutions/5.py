import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
(N, M) = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
abc = [list(map(int, input().split())) for _ in range(M)]
for (a, b, c) in abc:
    G[a][b] = c
    G[b][a] = c
cost = floyd_warshall(csr_matrix(G))
cnt = 0
for (a, b, c) in abc:
    if cost[a][b] < c:
        cnt += 1
print(cnt)
