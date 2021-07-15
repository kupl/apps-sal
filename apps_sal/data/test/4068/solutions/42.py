n,m = list(map(int,input().split()))
MOD=1000000007

dp=[0]*(n+1)
dp[0]=1

for _ in range(m):
    dp[int(input())]=-1

for i in range(n+1):
    if dp[i]==-1:
        continue

    if i+1<=n and dp[i+1]!=-1:
        dp[i+1]=(dp[i+1]+dp[i])%MOD
    if i+2<=n and dp[i+2]!=-1:
        dp[i+2]=(dp[i+2]+dp[i])%MOD

print((dp[-1]))

