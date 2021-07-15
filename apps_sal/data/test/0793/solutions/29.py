
#50 ABC130E
n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
mod=10**9+7

import numpy as np
t=np.array(t,dtype=np.int64)
dp=np.ones(m+1,dtype=np.int64)

for a in s:
	dp[1:]=((dp[:-1]*(t==a)).cumsum()+dp[1:])%mod
print(dp[-1])
