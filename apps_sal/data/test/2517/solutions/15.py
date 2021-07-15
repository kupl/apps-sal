from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations
n,m,r,*L=map(int,open(0).read().split())
f=floyd_warshall(csr_matrix((L[r+2::3],(L[r::3],L[r+1::3])),(n+1,n+1)),0)
print(int(min(sum(f[s,t]for s,t in zip(o,o[1:]))for o in permutations(L[:r]))))
