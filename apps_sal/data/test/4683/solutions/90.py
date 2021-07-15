import numpy as np
n=int(input())
a= sorted(map(int,input().split()))
b=np.cumsum(a)
c=0
mod=10**9+7
for i in range(n-1):
    c+=int(a[i])*(int(b[-1])-int(b[i]))
    c%=mod
print(c)
