s = input()
n = len(s)
mod = 10**9 + 7
dp = [[0] * 3 for _ in range(n)]
# dp[i][0] count of A's in all possible strings u generate till i
# dp[i][1] count of AB's ''
# dp[i][2] count of ABC's ''
cnt = 1
for i in range(n):
    if s[i] == '?':
        if i > 0:
            dp[i][2] = dp[i - 1][1] + 3 * dp[i - 1][2]
            dp[i][2] %= mod
            dp[i][1] = dp[i - 1][0] + 3 * dp[i - 1][1]
            dp[i][1] %= mod
            dp[i][0] = 3 * dp[i - 1][0] + 1 * cnt
            dp[i][0] %= mod
        else:
            dp[i][0] = 1
        cnt *= 3
        cnt %= mod
    elif s[i] == 'C':
        if i > 0:
            dp[i][2] = dp[i - 1][1] + dp[i - 1][2]
            dp[i][2] %= mod
            dp[i][1] = dp[i - 1][1]
            dp[i][0] = dp[i - 1][0]
    elif s[i] == 'B':
        if i > 0:
            dp[i][2] = dp[i - 1][2]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] %= mod
            dp[i][0] = dp[i - 1][0]
    elif s[i] == 'A':
        if i > 0:
            dp[i][2] = dp[i - 1][2]
            dp[i][1] = dp[i - 1][1]
            dp[i][0] = dp[i - 1][0] + 1 * cnt
            dp[i][0] %= mod
        else:
            dp[0][0] = 1

print((dp[-1][2] % mod))
