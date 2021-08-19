from sys import stdin
n = int(stdin.readline().strip())
s = list(map(int, stdin.readline().strip().split()))
dp = [[10 ** 15, 10 ** 15] for i in range(n)]
dp[0][0] = abs(s[0] - 1)
dp[0][1] = abs(s[0] - -1)
for i in range(1, n):
    un = abs(s[i] - 1)
    mun = abs(s[i] - -1)
    dp[i][0] = min(dp[i - 1][0] + un, dp[i - 1][1] + mun)
    dp[i][1] = min(dp[i - 1][1] + un, dp[i - 1][0] + mun)
print(dp[-1][0])
