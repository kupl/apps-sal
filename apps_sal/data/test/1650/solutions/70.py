l = input()
mod = 10**9+7

n = len(l)

dp = [[0]*2 for i in range(n)]

dp[0][0] = 1
dp[0][1] = 2

for i in range(1,n):
    dp[i][0] = dp[i-1][0]*3
    if l[i]=='1':
        dp[i][0] += dp[i-1][1]
        dp[i][1] = dp[i-1][1]*2
    else:
        dp[i][1] = dp[i-1][1]

    dp[i][0] %= mod
    dp[i][1] %= mod

ans = dp[n-1][0]+dp[n-1][1]
print((ans%mod))

