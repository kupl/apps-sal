from sys import stdin


def main():
    readline = stdin.readline
    mod = 10**9 + 7
    n = int(readline())

    A = 0
    T = 1
    G = 2
    C = 3
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
    dp[0][T][T][T] = 1
    for i in range(1, n + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == A and k == G and l == C:
                            pass
                        elif j == A and k == C and l == G:
                            pass
                        elif j == G and k == A and l == C:
                            pass
                        elif m == A and k == G and l == C:
                            pass
                        elif m == A and j == G and l == C:
                            pass
                        else:
                            dp[i][j][k][l] += dp[i - 1][m][j][k]
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod

    print(ans)


def __starting_point():
    main()


__starting_point()
