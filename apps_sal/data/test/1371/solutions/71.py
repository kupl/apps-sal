n = int(input())
mod = 10**9 + 7

if n <= 2:
    print(0)
    return

dp = [0 for i in range(n + 1)]
dp[0] = 1

for i in range(3, n + 1):
    dp[i] = (dp[i - 3] + dp[i - 1]) % mod

print(dp[n] % mod)
