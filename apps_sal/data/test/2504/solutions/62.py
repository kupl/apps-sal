import numpy as np

from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

N, M, L = list(map(int, input().split()))

if M == 0:
    Q = int(input())
    for _ in range(Q):
        print((-1))
    return

R = np.array([tuple(map(int, input().split())) for _ in range(M)])
matr = csr_matrix((R[:, 2], (R[:, 0] - 1, R[:, 1] - 1)), shape=(N, N))
way = floyd_warshall(matr, directed=False).astype(int)

way = np.where((way >= 0) & (way <= L), 1, 0)
matr_replenishment = csr_matrix(way)
way_replenishment = floyd_warshall(matr_replenishment, directed=False).astype(int).tolist()

Q = int(input())
for _ in range(Q):
    S, T = list(map(int, input().split()))
    print((res - 1 if (res := way_replenishment[S - 1][T - 1]) >= 0 else -1))

