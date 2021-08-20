n = int(input())
mod = 10 ** 9 + 7
dp = [0] * n
dp[0] = 1
for i in range(n):
    for j in range(i - 2):
        dp[i] += dp[j]
        dp[i] %= mod
dp[n - 1] = 0
dp[n - 2] = 0
print(sum(dp) % mod)
