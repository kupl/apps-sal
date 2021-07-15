import numpy as np
n=int(input())
a= sorted(map(int,input().split()))
b=np.cumsum(a,dtype=np.int64)
c=0
mod=10**9+7
for i in range(n-1):
    c+=(a[i]%mod)*((b[-1]-b[i])%mod)
    c%=mod
print(c)
