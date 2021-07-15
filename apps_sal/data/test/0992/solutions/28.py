import numpy as np
n,s=map(int, input().split( ))
*a,=map(int, input().split( ))
l=min(s+1,3001)
dp=np.zeros(l,dtype = int)
dp[0]=1
mod=998244353
ans=0
cnt=0
for ai in a:
    #dp2=dp.copy()
    dp2=dp[:-ai].copy()
    dp*=2
    dp[ai:]+=dp2#[:-ai]
    #ans+=dp[s]*pow(2,n-cnt,mod)
    #dp=dp2
    #ans%=mod
    dp%=mod
print(dp[s])
