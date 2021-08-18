from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


"""
点(x,y) を、辺x-yと見て二部グラフとみなす
"""

N = int(readline())
XY = np.array(read().split(), np.int32)

U = 10**5 + 100
X = XY[::2]
Y = XY[1::2]
graph = csr_matrix((np.ones(N), (X, Y + U)), (U + U, U + U))
Ncomp, comp = connected_components(graph)

comp_x = np.bincount(comp[:U], minlength=Ncomp)
comp_y = np.bincount(comp[U:], minlength=Ncomp)
comp_E = np.bincount(comp[X], minlength=Ncomp)

answer = (comp_x * comp_y - comp_E).sum()
print(answer)
