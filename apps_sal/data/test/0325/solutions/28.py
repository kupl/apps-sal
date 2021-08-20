import numpy as np
from collections import defaultdict
from scipy.sparse.csgraph import bellman_ford, connected_components
from scipy.sparse import csr_matrix
(N, M, P) = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
ABC_max = defaultdict(int)
for (a, b, c) in ABC:
    ABC_max[a, b] = max(ABC_max[a, b], c)
ABC = np.array([[a, b, c] for ((a, b), c) in ABC_max.items()], np.int64)
A = ABC[:, 0] - 1
B = ABC[:, 1] - 1
C = ABC[:, 2] - P
L = csr_matrix((C, (A, B)), (N, N))
L[N - 1, 0] = 1
(_, label) = connected_components(L, connection='strong')
label = np.arange(N)[label == label[0]]
ABC = ABC[np.isin(ABC[:, :2], label + 1).all(axis=1)]
A = ABC[:, 0] - 1
B = ABC[:, 1] - 1
C = ABC[:, 2] - P
L = csr_matrix((-C, (A, B)), (N, N))
try:
    dist = bellman_ford(L, indices=0).astype(np.int64)
    print(max(0, -dist[-1]))
except:
    print(-1)
