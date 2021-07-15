import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.csgraph import shortest_path

n,m,limit=map(int,input().split())
G=np.zeros((n,n),dtype=np.int64)
for i in range(m):
    a,b,cost=map(int,input().split())
    G[a-1,b-1]=cost
    G[b-1,a-1]=cost
G=shortest_path(G,method='FW')
for c in range(n):
    for l in range(n):
        if G[c][l]<=limit:
            G[c][l]=1
        else:
            G[c][l]=0
G=shortest_path(G,method='FW')
q=int(input())
Q=[map(int,input().split())for i in range(q)]
for a,b in Q:
    print(int(G[a-1][b-1])-1 if G[a-1][b-1]<10**18 else -1)
