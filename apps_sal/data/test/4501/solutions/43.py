N, A = map(int, input().split())
X = [int(x) for x in input().split()]

dp = [[0] * (N * A + 1) for _ in range(N + 1)]  # dp[i][j]:i枚の和がjとなるようなカードの選び方
dp[0][0] = 1
for x in X:
    for i in reversed(range(1, N + 1)):
        for j in reversed(range(N * A + 1)):
            if j < x:
                continue
            dp[i][j] += dp[i - 1][j - x]
ans = sum(dp[k][k * A] for k in range(1, N + 1))
print(ans)
