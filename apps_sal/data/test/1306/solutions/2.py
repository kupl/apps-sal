n, h = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0] * 2000 for i in range(n)]

dp[0][0] = 1 if a[0] in (h, h - 1) else 0
dp[0][1] = 1 if a[0] == h - 1 else 0

for i in range(1, n):
    opn = h - a[i]
    if opn >= 0:
        dp[i][opn] += dp[i - 1][opn]
        if opn > 0:
            dp[i][opn] += dp[i - 1][opn - 1]
        dp[i][opn] %= mod
    opn -= 1
    if opn >= 0:
        dp[i][opn] += dp[i - 1][opn + 1] * (opn + 1) + dp[i - 1][opn] + dp[i - 1][opn] * opn
        dp[i][opn] %= mod

print(dp[-1][0])
