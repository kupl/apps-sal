import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.csgraph import shortest_path
M=49*50+1
n,m,s=map(int,input().split())
s=min(s,M-1)
G=lil_matrix((n*M,n*M))
for _ in range(m):
    a,b,silver,time=map(int,input().split())
    a-=1
    b-=1
    for i in range(silver,M):
        G[a*M+i,b*M+i-silver]=time
        G[b*M+i,a*M+i-silver]=time
for i in range(n):
    silver,time=map(int,input().split())
    for j in range(M-1):
        G[i*M+j,i*M+min(j+silver,M-1)]=time
G=G.tocsr()
G=shortest_path(G,method='D',indices=s)

for i in range(1,n):
    ans=np.min(G[i*M:i*M+M])
    print(int(ans))
