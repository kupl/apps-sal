N,S=map(int,input().split())
A=list(map(int,input().split()))
import numpy as np
d=np.zeros((N+1,S+1),dtype=np.int64)
d[0,0]=1
m=998244353
for i in range(N):
    d[i+1]=d[i]*2%m
    d[i+1,A[i]:]=(d[i+1,A[i]:]+d[i,:-A[i]])%m
print(d[-1,-1])
