n,m,q=map(int,input().split())
import numpy as np
dim2=np.zeros((n+1,n+1),dtype='int8')

for _ in range(m):
    l,r=map(int,input().split())
    dim2[l][r]+=1

dim2=np.cumsum(dim2,axis=0)

dim2=np.cumsum(dim2,axis=1)
for _ in range(q):
    p,q=map(int, input().split())
    ans=dim2[q][q]-dim2[q][p-1]-dim2[p-1][q]+dim2[p-1][p-1]
    print(ans)
