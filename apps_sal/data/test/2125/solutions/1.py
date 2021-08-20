def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    m = int(buflist[1])
    blanket = []
    for i in range(n):
        buf = input()
        blanket.append(buf)
    dp = [[]]
    for j in range(m + 1):
        dp[0].append([0, (0, '0'), (0, '0'), (0, '0'), 0])
    for i in range(n):
        dp.append([[0, (0, '0'), (0, '0'), (0, '0'), 0]])
    for i in range(n):
        for j in range(m):
            dp[i + 1].append([0, (0, None), (0, None), (0, None), 0])
            dp[i + 1][j + 1][0] = dp[i + 1][j][0] + dp[i][j + 1][0] - dp[i][j][0]
            if blanket[i][j] == dp[i][j + 1][1][1]:
                dp[i + 1][j + 1][1] = (dp[i][j + 1][1][0] + 1, dp[i][j + 1][1][1])
                dp[i + 1][j + 1][2] = dp[i][j + 1][2]
                dp[i + 1][j + 1][3] = dp[i][j + 1][3]
            else:
                dp[i + 1][j + 1][1] = (1, blanket[i][j])
                dp[i + 1][j + 1][2] = dp[i][j + 1][1]
                dp[i + 1][j + 1][3] = dp[i][j + 1][2]
            if dp[i + 1][j + 1][1][0] == dp[i + 1][j + 1][2][0] and dp[i + 1][j + 1][2][0] <= dp[i + 1][j + 1][3][0]:
                if dp[i + 1][j + 1][1] == dp[i + 1][j][1] and dp[i + 1][j + 1][2] == dp[i + 1][j][2] and (dp[i + 1][j + 1][3][1] == dp[i + 1][j][3][1]):
                    dp[i + 1][j + 1][4] = dp[i + 1][j][4]
                dp[i + 1][j + 1][0] += dp[i + 1][j + 1][4] + 1
                dp[i + 1][j + 1][4] += 1
    print(dp[n][m][0])


def __starting_point():
    main()


__starting_point()
