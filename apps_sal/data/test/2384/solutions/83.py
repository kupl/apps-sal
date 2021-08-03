from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
m = n // 2
INF = 10**18
dp = [defaultdict(lambda: -INF) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i // 2 - 1, (i + 1) // 2 + 1):
        if j == 1:
            dp[i][j] = max(dp[i - 1][j], A[i - 1])
        elif 0 <= i - 2 and 0 <= j <= m:
            dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + A[i - 1])
print(dp[-1][m])
