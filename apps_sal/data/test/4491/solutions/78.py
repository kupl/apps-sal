n = int(input())
a = [list(map(int, input().split())) for i in range(2)]
dp = [[0] * (n + 1) for _ in range(3)]
for i in range(1, 3):
    for j in range(1, n + 1):
        now = a[i - 1][j - 1]
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + now
print(dp[-1][-1])
