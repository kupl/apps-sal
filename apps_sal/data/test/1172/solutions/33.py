s = input()
n = len(s)
mod = 10 ** 9 + 7
dp = [[0] * 4 for _ in range(n + 1)]
dp[n][3] = 1
for i in reversed(list(range(n))):
    for j in reversed(list(range(4))):
        if j == 3:
            if s[i] == '?':
                m = 3
            else:
                m = 1
            dp[i][j] += m * dp[i + 1][j]
        else:
            if s[i] == '?':
                m1 = 3
            else:
                m1 = 1
            if j == 0:
                if s[i] == 'A' or s[i] == '?':
                    m2 = 1
                else:
                    m2 = 0
            elif j == 1:
                if s[i] == 'B' or s[i] == '?':
                    m2 = 1
                else:
                    m2 = 0
            elif s[i] == 'C' or s[i] == '?':
                m2 = 1
            else:
                m2 = 0
            dp[i][j] += m1 * dp[i + 1][j] + m2 * dp[i + 1][j + 1]
        dp[i][j] %= mod
print(dp[0][0] % mod)
