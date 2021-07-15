s = int(input())

mod = 10 ** 9 + 7

dp = [0] * (s + 1)
dp[0] = 1
dp[1] = 0

if s > 1:
    dp[2] = 0

    for i in range(3, s + 1):
        dp[i] = sum(dp[:i - 2]) % mod

print(dp[s])
