import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
from operator import itemgetter

N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y, i))

data = [10, 20, 30, 40]
row = [0, 0, 1, 1]
col = [1, 2, 0, 2]

#print(csr_matrix((data, (row, col))).toarray())

data = []
row = []
col = []

P.sort()
D = {}
for i in range(N - 1):
    a, b, p = P[i]
    c, d, q = P[i + 1]
    cost = min(abs(a - c), abs(b - d))
    data.append(cost)
    row.append(p)
    col.append(q)
    data.append(cost)
    row.append(q)
    col.append(p)
    D[(p, q)] = cost
    D[(q, p)] = cost

P.sort(key=itemgetter(1))
for i in range(N - 1):
    a, b, p = P[i]
    c, d, q = P[i + 1]
    if (p, q) in D:
        continue
    cost = min(abs(a - c), abs(b - d))
    data.append(cost)
    row.append(p)
    col.append(q)
    data.append(cost)
    row.append(q)
    col.append(p)
    D[(p, q)] = cost
    D[(q, p)] = cost

coo = coo_matrix((data, (row, col)), (N, N))
mst = minimum_spanning_tree(coo)
print(int(mst.sum()))
