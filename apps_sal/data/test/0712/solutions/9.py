import sys
try:
    while True:
        dp = [[0 for j in range(2001)] for i in range(2001)] * 2001
        (n, p, t) = map(float, input().split(' '))
        n = int(n)
        t = int(t)
        dp[0][0] = 1
        for i in range(1, t + 1, 1):
            for j in range(0, n + 1, 1):
                if j == n:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] * (1 - p)
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * p
        ans = 0
        for i in range(n + 1):
            ans += i * dp[t][i]
        print(ans)
except EOFError:
    pass
