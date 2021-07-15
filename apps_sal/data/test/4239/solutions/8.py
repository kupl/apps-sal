N=int(input())
INF=10**10
dp=[INF]*(N+1)
dp[0]=0
for i in range(N+1):
    if i+1<=N: dp[i+1]=min(dp[i+1],dp[i]+1)
    j=1
    while i+6**j<=N:
        dp[i+6**j]=min(dp[i+6**j],dp[i]+1)
        j+=1
    j=1
    while i+9**j<=N:
        dp[i+9**j]=min(dp[i+9**j],dp[i]+1)
        j+=1
print(dp[N])
