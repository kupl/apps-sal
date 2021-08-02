import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import itertools
I = [int(_) for _ in open(0).read().split()]
N, M, R = I[:3]
r = np.array(I[3:3 + R])
ABC = I[3 + R:]
F = floyd_warshall(csr_matrix((ABC[2::3], (ABC[::3], ABC[1::3])), (N + 1, N + 1)), 0).astype(np.int64)
ans = float('inf')
for root in itertools.permutations(r, R):
    ans = min(ans, sum(F[i, j] for i, j in zip(root, root[1:])))
print(ans)
