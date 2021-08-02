import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
n = int(input())
m = 10**5 + 5
l = []
lx = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b + m, 1))
    lx.append(a)
edge = np.array(l, dtype=np.int64).T
graph = csr_matrix(((edge[2], edge[:2] - 1)), (2 * m, 2 * m))
n, labels = connected_components(graph)
lx = np.array(lx)
x = np.bincount(labels[:m], minlength=n)
y = np.bincount(labels[m:], minlength=n)
e = np.bincount(labels[lx], minlength=n)
print((x * y - e).sum())
