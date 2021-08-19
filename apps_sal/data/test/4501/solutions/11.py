(n, a) = list(map(int, input().split()))
xxx = list(map(int, input().split()))
limit = a * n
dp = [[0] * (limit + 1) for i in range(n + 1)]
dp[0][0] = 1
for (i, x) in enumerate(xxx):
    if x > limit:
        continue
    for j in range(i, -1, -1):
        for k in range(limit - x, -1, -1):
            dp[j + 1][k + x] += dp[j][k]
print(sum((dp[i][i * a] for i in range(1, n + 1))))
