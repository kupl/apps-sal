N = int(input())

MOD = 10**9 + 7
dp = [[0] * (2020 + 1) for _ in range(2020 + 1)]
dp[1][1] = 1
ans = 0
for i in range(2, N + 2):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
        if (i + j) % 2 == 1:
            ans = (ans + dp[i][j]) % MOD
print(ans)

