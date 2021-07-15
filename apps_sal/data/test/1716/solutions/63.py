import numpy as np 
N,M,Q=map(int, input().split())
a=np.array([[0]*N for i in range(N)])

for i in range(M):
  l,r=map(int, input().split())
  a[l-1][r-1]+=1
a=a.cumsum(axis=0).cumsum(axis=1)

for i in range(Q):
  p,q=map(int, input().split())
  if p==1:
    ans=a[q-1][q-1]
  else:
    ans=a[q-1][q-1]-a[p-2][q-1]
  print(ans)
