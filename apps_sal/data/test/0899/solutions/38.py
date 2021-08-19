import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
(N, M, *ABC) = [int(_) for _ in open(0).read().split()]
ABC = np.array(ABC)
F = floyd_warshall(csr_matrix((ABC[2::3], (ABC[::3], ABC[1::3])), (N + 1, N + 1)), 0)
print(np.sum(F[ABC[::3], ABC[1::3]] != ABC[2::3]))
