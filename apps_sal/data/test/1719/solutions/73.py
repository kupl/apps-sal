import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())
    dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]
    dp[0][0][0][0] = 1
    for n in range(N):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    for l in range(1, 5):
                        if i == 1 and j == 2 and (l == 3):
                            continue
                        if i == 1 and k == 2 and (l == 3):
                            continue
                        if j == 1 and k == 2 and (l == 3):
                            continue
                        if j == 2 and k == 1 and (l == 3):
                            continue
                        if j == 1 and k == 3 and (l == 2):
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
