s = int(input())
MOD = 10 ** 9 + 7
dp = [0] * (s + 1)
dp[0] = 1
for i in range(s + 1):
    for j in range(0, i - 3 + 1):
        dp[i] += dp[j]
        dp[i] %= MOD
print(dp[s])
