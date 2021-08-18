import sys
input = sys.stdin.readline

t = 1
for _ in range(t):
    n, m = (int(x) for x in input().split())
    mat = [input() for x in range(n)]
    dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if mat[i][j] == '
            dp[i][j] = 0

            elif i == n - 1 and j == m - 1:
                dp[i][j] = 1

            elif i == n - 1:
                dp[i][j] = dp[i][j + 1]

            elif j == m - 1:
                dp[i][j] = dp[i + 1][j]

            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    if dp[0][0] == 0:
        print(0)
        break

    ans = 2
    r1, c1, r2, c2 = 0, 0, 0, 0
    for i in range(n + m - 2 - 1):
        if dp[r1 + 1][c1] != 0:
            r1 += 1
        else:
            c1 += 1

        if dp[r2][c2 + 1] != 0:
            c2 += 1
        else:
            r2 += 1

        if r1 == r2 and c1 == c2:
            ans = 1
            break

    print(ans)
