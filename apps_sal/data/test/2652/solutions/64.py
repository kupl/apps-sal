from operator import itemgetter
from scipy.sparse import csr_matrix
import numpy as np

N = int(input())

XY = [[i] + [int(x) for x in input().split()] for i in range(N)]

edge = set()
for key in [itemgetter(1),itemgetter(2)]:
  XY.sort(key = key)
  for i in range(N-1):
    i1,x1,y1 = XY[i]
    i2,x2,y2 = XY[i+1]
    d = min(abs(x1-x2),abs(y1-y2))
    edge.add((i1,i2,d))
    
# csr形式に直す
row,col,value = zip(*edge)
value = np.array(value,dtype=int)
graph = csr_matrix((value,(row,col)),shape=(N,N))

# 最小全域木
from scipy.sparse.csgraph import minimum_spanning_tree
tree = minimum_spanning_tree(graph, overwrite = True).astype(int)
answer = tree.sum()
print(answer)
