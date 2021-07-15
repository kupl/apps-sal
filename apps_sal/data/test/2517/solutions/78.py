from itertools import *
from scipy.sparse.csgraph import *
import numpy as np
N,M,R = map(int,input().split())
T = list(map(int,input().split()))
E = [list(map(int,input().split())) for m in range(M)]
G = np.zeros((N,N))
A = []

for a,b,c in E:
  G[a-1][b-1] = c
  G[b-1][a-1] = c

F = floyd_warshall(G)

for P in permutations(T):
  A+=[sum(F[P[r]-1][P[r+1]-1] for r in range(R-1))]

print(int(min(A)))
