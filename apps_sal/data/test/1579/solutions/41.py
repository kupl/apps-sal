import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

"""
点(x,y) を、辺x-yと見て二部グラフとみなす
"""

N = int(readline())
XY = np.array(read().split(),np.int32)

U = 10**5 + 100
X = XY[::2]; Y = XY[1::2]
graph = csr_matrix((np.ones(N),(X,Y+U)),(U+U,U+U))
Ncomp,comp = connected_components(graph)

comp_x=np.bincount(comp[:U],minlength=Ncomp) # 連結成分に含まれるx座標の個数
comp_y=np.bincount(comp[U:],minlength=Ncomp) # 連結成分に含まれるx座標の個数
comp_E=np.bincount(comp[X],minlength=Ncomp) # 連結成分に含まれる辺の個数

answer = (comp_x * comp_y - comp_E).sum()
print(answer)
