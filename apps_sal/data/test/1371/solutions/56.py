s = int(input())

mod = 10**9 + 7

if s < 3:
    print(0)
    return

dp = [0] * (s + 1)
dp[0] = 1

for i in range(3, s + 1):
    dp[i] = (dp[i - 3] + dp[i - 1]) % mod

print(dp[s])
