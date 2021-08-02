import scipy.sparse as sparse
from scipy.sparse.csgraph import shortest_path
import numpy as np

n, x, y = [int(i) for i in input().split()]
x -= 1
y -= 1

one = np.ones((2, n), dtype=int)
c = sparse.spdiags(one, np.array([-1, 1]), n, n, format='lil')

c[x, y], c[y, x] = 1, 1

c = c.tocsr()

path = shortest_path(c, directed=False, unweighted=True)

u, counts = np.unique(path, return_counts=True)
counts = counts // 2

for i in range(1, int(u[-1]) + 1):
    print((counts[i]))
for i in range(int(u[-1]) + 1, n):
    print((0))
