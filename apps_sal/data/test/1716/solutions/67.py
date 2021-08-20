(n, m, q) = map(int, input().split())
train = []
for _ in range(m):
    (l, r) = map(int, input().split())
    train.append((l, r))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for [l, r] in train:
    dp[l][r] += 1
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] += dp[i + 1][j]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] += dp[i][j + 1]
for i in range(q):
    (l, r) = map(int, input().split())
    print(dp[r][r] - dp[l - 1][r] - dp[r][l - 1] + dp[l - 1][l - 1])
