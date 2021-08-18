from sys import stdin

input = stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(max(a[0], -a[0]))
        return
    NINF = -10 ** 15
    dp = [[[[NINF] * 2 for i in range(2)] for j in range(3)] for k in range(n)]
    dp[0][n % 3][0][1] = a[0]
    dp[0][(n + 1) % 3][0][0] = -a[0]
    for i in range(n - 1):
        for j in range(3):
            for k in range(2):
                for l in range(2):
                    if dp[i][j][k][l] > NINF:
                        dp[i + 1][j][k or l == 1][1] = max(dp[i + 1][j][k or l == 1][1], dp[i][j][k][l] + a[i + 1])
                        dp[i + 1][(j + 1) % 3][k or l == 0][0] = max(dp[i + 1][(j + 1) % 3][k or l == 0][0],
                                                                     dp[i][j][k][l] - a[i + 1])

    print(max(dp[n - 1][1][1][1], dp[n - 1][1][1][0]))


def __starting_point():
    solve()


__starting_point()
