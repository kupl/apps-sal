from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
dp = [defaultdict(lambda: -float('inf')) for _ in range(n)]
for i in range(n):
    dp[i][0] = 0
for (i, a) in enumerate(a):
    for j in range(n // 2 - (n - i) // 2, i // 2 + 2):
        dp[i][j] = max(dp[i - 2][j], dp[i - 2][j - 1] + a, dp[i - 1][j])
print(dp[-1][n // 2])
