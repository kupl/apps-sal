s = int(input())
dp = [0] * (s + 4)
mod = 1000000007
dp[0] = 1
dp[1] = 0
dp[2] = 0
dp[3] = 1
if s < 4:
    print(dp[s])
else:
    dp[0] = 1
    dp[1] = 0
    dp[2] = 0
    dp[3] = 1
    for i in range(4, s + 1):
        dp[i] = (dp[i - 1] + dp[i - 3]) % mod
    print(dp[s])
