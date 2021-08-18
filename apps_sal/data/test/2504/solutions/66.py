from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
from scipy.sparse import csr_matrix

N, M, L = list(map(int, input().split()))
V = [[10**12 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a, b = a - 1, b - 1
    V[a][b] = c
    V[b][a] = c

G = csgraph_from_dense(V, null_value=10**12)
d = floyd_warshall(G)

V2 = [[10**9 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if 0 < d[i][j] <= L:
            V2[i][j] = 1

G2 = csgraph_from_dense(V2, null_value=10**9)
d2 = floyd_warshall(G2)

Q = int(input())
for _ in range(Q):
    s, t = list(map(int, input().split()))
    s, t = s - 1, t - 1
    print((int(d2[s][t]) - 1 if d2[s][t] < 1000 else -1))
