from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np
(n, m) = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]
(row, col, data) = zip(*abc)
L = csr_matrix((data, (row, col)), shape=(n + 1, n + 1))
(_, path) = dijkstra(L, directed=False, return_predecessors=True)
(s, e) = np.where(path > 0)
path_use = set(map(tuple, np.vstack([path[s, e], e]).T))
print(m - len(path_use) // 2)
