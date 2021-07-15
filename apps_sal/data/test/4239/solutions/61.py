n = int(input())

dp = [10**6 for _ in range(n+1)]
dp[0] = 0

for i in range(n+1):
    j6 = 1
    while i+j6<=n:
        dp[i+j6] = min(dp[i]+1,dp[i+j6])
        j6 *= 6
    j9 = 1
    while i+j9<=n:
        dp[i+j9] = min(dp[i]+1,dp[i+j9])
        j9 *= 9
print((dp[n]))

