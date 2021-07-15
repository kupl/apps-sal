import numpy as np 
N=int(input())
a=np.array(list(map(int, input().split())))
ans=0
mod=10**9+7
for i in range(60):
   s=np.count_nonzero(a>>i&1)
   ans+=pow(2,i,mod)*s*(N-s)%mod
   ans%=mod
print(ans)
