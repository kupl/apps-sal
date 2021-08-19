import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())

    # dp[i文字目][3文字前][2文字前][1文字前]
    dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]
    dp[0][0][0][0] = 1

    # _,A,G,C,T = 0,1,2,3,4
    for n in range(N):
        # 3文字前
        for i in range(5):
            # 2文字前
            for j in range(5):
                # 1文字前
                for k in range(5):
                    # 最後の文字
                    for l in range(1, 5):
                        # AG*C
                        if i == 1 and j == 2 and l == 3:
                            continue
                        # A*GC
                        if i == 1 and k == 2 and l == 3:
                            continue
                        # *AGC
                        if j == 1 and k == 2 and l == 3:
                            continue
                        # *GAC
                        if j == 2 and k == 1 and l == 3:
                            continue
                        # *ACG
                        if j == 1 and k == 3 and l == 2:
                            continue
                        dp[n + 1][j][k][l] += dp[n][i][j][k]
                        dp[n + 1][j][k][l] %= mod
    res = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                res += dp[-1][i][j][k]
                res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
