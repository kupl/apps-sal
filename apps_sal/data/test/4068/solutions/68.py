import numpy as np
N,M=map(int,input().split())
A=set([int(input()) for _ in range(M)])

mod=10**9+7

dp=np.zeros(N+1)
dp[0]=1
if 1 not in A:
    dp[1]=1
else:
    dp[1]=0

for i in range(2,N+1):
    if i in A:
        continue
    dp[i]=dp[i-1]+dp[i-2]
    dp[i]%=mod

print(int(dp[N]))
