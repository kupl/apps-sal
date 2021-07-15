s = int(input())
mod = 1000000007
dp = [0]*(s+1)
dp[0] = 1
for i in range(3,s+1):
    for j in range(i-2):
        dp[i] += dp[j]
        dp[i] %= mod
print(dp[s])
