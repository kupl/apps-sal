import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


# ===CODE===


def main():
    h, w, k = ns()
    dp = [[0 for _ in range(w)] for __ in range(h + 1)]
    dp[0][0] = 1
    fibo = [1, 2]
    for i in range(10):
        fibo.append(fibo[-1] + fibo[-2])

    for y in range(1, h + 1):
        for x in range(w):
            if x == 0:
                # from U
                dp[y][x] += dp[y - 1][x] * fibo[max(0, w - 1 - 1)]
                if w > 1:
                    # from R
                    dp[y][x] += dp[y - 1][x + 1] * fibo[max(0, w - 1 - 2)]
            elif x == w - 1:
                # from U
                dp[y][x] += dp[y - 1][x] * fibo[max(0, w - 1 - 1)]
                if w > 1:
                    # from L
                    dp[y][x] += dp[y - 1][x - 1] * fibo[max(0, w - 1 - 2)]
            else:
                # from U
                dp[y][x] += dp[y - 1][x] * fibo[x - 1] * fibo[max(0, w - 1 - x - 1)]
                # from L
                dp[y][x] += dp[y - 1][x - 1] * fibo[max(0, x - 1 - 1)] * fibo[max(0, w - 1 - x - 1)]
                # from R
                dp[y][x] += dp[y - 1][x + 1] * fibo[x - 1] * fibo[max(0, w - 1 - x - 2)]
            dp[y][x] %= MOD

    print((dp[h][k - 1]))


def __starting_point():
    main()


__starting_point()
