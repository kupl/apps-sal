from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np
(N, M) = list(map(int, input().split()))
l = [np.array([0] * N) for i in range(N)]
for i in range(M):
    tmp = list(map(int, input().split()))
    l[tmp[0] - 1][tmp[1] - 1] = tmp[2]
    l[tmp[1] - 1][tmp[0] - 1] = tmp[2]
l2 = csr_matrix(l)
l2 = floyd_warshall(l2)
ans = 0
for i in range(N):
    for j in range(i):
        if l[i][j] != l2[i][j] and l[i][j] != 0:
            ans += 1
print(ans)
