MOD = 10**9 + 7
S = int(input())

dp = [0] * (S + 1)
dp[0] = 1
for i in range(1, S + 1):
    for j in range(0, (i - 3) + 1):
        dp[i] += dp[j]
        dp[i] %= MOD

print(dp[S])
