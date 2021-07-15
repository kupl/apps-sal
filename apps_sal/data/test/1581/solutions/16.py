#無理ぞ
n,k=map(int, input().split())
a,b=[],[]
i=1

while i*i<=n:
    a.append(i)
    b.append(n//i)
    i+=1
    
if a[-1]==b[-1]:
    b.pop()
a+=b[::-1]
import numpy as np
dp=np.array(a)
dp[1:]-=dp[:-1]
ini=np.copy(dp)
del a
del b
mod=10**9+7
for _ in range(k-1):
    pre=np.cumsum(dp)
    dp=ini*pre[::-1]
    dp%=mod
print(sum(dp)%mod)
