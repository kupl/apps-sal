n,s=map(int,input().split())
a=[int(j)for j in input().split()]
mod=998244353
ans=0
import numpy as np
dp=np.zeros(3001,np.int64)
for i in a:
    dp[0]+=1
    dp[i:]+=dp[:-i].copy()
    dp%=mod
    ans+=dp[s]
    ans%=mod
print(ans)
