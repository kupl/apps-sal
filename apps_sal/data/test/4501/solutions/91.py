N, A = list(map(int, input().split()))
lst = [int(x) - A for x in input().split()]
dp = [[0] * (100 * N + 1) for _ in range(N + 1)]
dp[0][50 * N] = 1
for i in range(N):
    for j in range(50, 100 * N + 1 - 50):
        dp[i + 1][j] = dp[i][j] + dp[i][j - lst[i]]
print((dp[N][50 * N] - 1))

