import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
INF = 10**12
N, M, L = map(int, input().split())

A = []
B = []
C = []
for i in range(M):
    a, b, c = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)
    C.append(c)
A = np.array(A)
B = np.array(B)
C = np.array(C)

graph = csr_matrix((C, (A, B)), (N, N))
d = floyd_warshall(graph, directed=False)

d[d <= L] = 1
d[d > L] = INF

d = floyd_warshall(d, directed=False)

Q = int(input())
for i in range(Q):
    s, t = map(int, input().split())
    if d[s - 1][t - 1] != INF:
        print(int(d[s - 1][t - 1]) - 1)
    else:
        print(- 1)
