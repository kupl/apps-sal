from scipy.sparse.csgraph import floyd_warshall
import numpy as np
from itertools import permutations

n,m,r = map(int,input().split())
rr = np.array(list(map(int,input().split()))) - 1

L = np.zeros((n,n),int)
for _ in range(m):
    a,b,c = map(int,input().split())
    L[a-1,b-1] = c

shortest = floyd_warshall(L, directed = False)

ans = float('inf')

for route in permutations(rr,len(rr)):
    ans = min(ans, shortest[route[:-1],route[1:]].sum())
print(int(ans))
