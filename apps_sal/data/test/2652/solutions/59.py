from scipy.sparse import *
from scipy.sparse.csgraph import *
N = int(input())
T = [[n] + list(map(int, input().split())) for n in range(N)]
P = set()
for i in [1, 2]:
    T.sort(key=lambda a: a[i])
    for j in range(1, N):
        (i0, x0, y0) = T[j - 1]
        (i1, x1, y1) = T[j]
        P.add((min(abs(x1 - x0), abs(y1 - y0)), i0, i1))
(d, i, j) = zip(*P)
G = csr_matrix((d, (i, j)), shape=(N, N))
print(int(minimum_spanning_tree(G).sum()))
