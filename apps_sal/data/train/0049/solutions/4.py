def f(n):
    if n == 0:
        return 1
    dp = [[[0] * 2 for j in range(4)] for z in range(len(n))]
    dp[0][3][0] = 1
    dp[0][2][0] = int(n[0]) - 1
    dp[0][2][1] = 1
    for i in range(1, len(n)):
        for j in range(4):
            if n[i] == '0':
                dp[i][j][0] += dp[i - 1][j][0]
                dp[i][j][1] += dp[i - 1][j][1]
            else:
                dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]
            for z in range(1, 10):
                if z < int(n[i]):
                    if j < 3:
                        dp[i][j][0] += dp[i - 1][j + 1][0] + dp[i - 1][j + 1][1]
                elif z == int(n[i]):
                    if j < 3:
                        dp[i][j][0] += dp[i - 1][j + 1][0]
                        dp[i][j][1] += dp[i - 1][j + 1][1]
                else:
                    if j < 3:
                        dp[i][j][0] += dp[i - 1][j + 1][0]

    res = 0
    for j in range(4):
        res += dp[len(n) - 1][j][0] + dp[len(n) - 1][j][1]
    return res

t = int(input())
while t:
    t -= 1
    l, r = list(map(int, input().split()))
    print(f(str(r)) - f(str(l - 1)))

