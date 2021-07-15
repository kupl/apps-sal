import itertools
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

int1 = lambda x: int(x) - 1

N, M, R = map(int, input().split())
T = sorted(list(map(int1, input().split())))
A = np.array([tuple(map(int, input().split())) for _ in range(M)]).T

matr = csr_matrix((A[2], (A[0] - 1, A[1] - 1)), shape=(N, N))
way = [dijkstra(matr, indices=t, directed=False)[T].astype(int).tolist() for t in T]

ans = float('inf')
for t in itertools.permutations(range(R)):
    tmp = 0
    for i in range(R - 1):
        tmp += way[t[i]][t[i + 1]]
    ans = min(ans, tmp)
print(ans)
