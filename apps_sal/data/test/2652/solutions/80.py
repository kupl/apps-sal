
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from operator import itemgetter
def resolve():
    N = int(input())
    XY = [[i] + [int(x) for x in input().split()] for i in range(N)]

    G = set()
    for key in [itemgetter(1), itemgetter(2)]:
        XY.sort(key=key)
        for i in range(N - 1):
            i1, x1, y1 = XY[i]
            i2, x2, y2 = XY[i + 1]
            d = min(abs(x1 - x2), abs(y1 - y2))
            G.add((i1, i2, d))    

    A, B, W = zip(*G)
    csr = csr_matrix((W, (A, B)), shape=(N, N))
    mst = minimum_spanning_tree(csr).astype(int)
    print(mst.sum())

def __starting_point():
    resolve()
__starting_point()
