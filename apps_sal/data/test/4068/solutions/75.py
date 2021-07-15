n,m=list(map(int,input().split()))
a=[int(input()) for i in range(m)]
a=set(a)
mod=10**9+7
dp=[0]*(n+7)
dp[0]=1
for i in range(n+1):
    if i+2 not in a: #2段先が壊れていない
        dp[i+2]+=dp[i]
    if i+1 not in a: #1段先が壊れていない
        dp[i+1]+=dp[i]
    dp[i+2]%=mod
    dp[i+1]%=mod
print((dp[n]%mod))

