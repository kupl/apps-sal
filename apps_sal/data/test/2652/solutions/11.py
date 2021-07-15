from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from operator import itemgetter

n = int(input()) 
ixy = [[i] + [int(x) for x in input().split()] for i in range(n)]

edge = set()

for key in [itemgetter(1),itemgetter(2)]:
    ixy.sort(key = key)
    for i in range(n-1):
        i1, i2 = ixy[i][0], ixy[i+1][0]
        x1, x2 = ixy[i][1], ixy[i+1][1]
        y1, y2 = ixy[i][2], ixy[i+1][2]
        d = min(abs(x2-x1), abs(y2-y1))
        edge.add((i1,i2,d))
    
row,col,value = zip(*edge)
csr_ = csr_matrix((value, (row,col)), shape=(n, n))
mst = minimum_spanning_tree(csr_, overwrite=True).astype(int)
print(mst.sum())
