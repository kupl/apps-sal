MOD = 10**9 + 7
n, oddness = [int(item) for item in input().split()]
# Oddness must be even
if oddness % 2 == 1:
    print(0)
    return
oddness //= 2
max_oddness = 1250 + n
max_pending = n // 2 + 2

dp = [[[0] * (max_oddness) for _ in range(max_pending)] for _ in range(n)]
dp[0][0][0] = 1
dp[0][1][1] = 1
for i in range(1, n):
    for j in range(min(i + 1, n // 2 + 1)):
        for k in range(oddness + 1):
            dp_ijk_prev = dp[i - 1][j][k]
            # Oddness increase by num of pending item
            # Do not connect
            dp[i][j + 1][k + j + 1] += dp_ijk_prev
            # Choose 2 from pending items
            if j > 0:
                dp[i][j - 1][k + j - 1] += dp_ijk_prev * j * j
            # Connect in line
            dp[i][j][k + j] += dp_ijk_prev
            # Choose 1 from pending items
            dp[i][j][k + j] += dp_ijk_prev * j * 2
            dp[i][j][k + j] %= MOD

print(dp[n - 1][0][oddness] % MOD)
