import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().split()])


# ===CODE===


def main():
    n, k = ns()
    a = na()

    max_len = 41
    popcount = [0] * max_len

    for ai in a:
        cnt = 0
        while ai > 0:
            if ai & 1:
                popcount[cnt] += 1
            ai >>= 1
            cnt += 1
    popcount.reverse()

    dp1 = [0 for _ in range(max_len + 1)]
    dp2 = [-1 for _ in range(max_len + 1)]

    for i in range(max_len):
        tmp = pow(2, max_len - 1 - i)
        ki = k >> (max_len - 1 - i) & 1

        one = popcount[i]
        zero = n - popcount[i]

        if ki:
            dp1[i + 1] = dp1[i] + zero * tmp
            dp2[i + 1] = dp1[i] + one * tmp
            if dp2[i] != -1:
                dp2[i + 1] = max(dp2[i + 1], dp2[i] + zero * tmp, dp2[i] + one * tmp)

        else:
            dp1[i + 1] = dp1[i] + one * tmp
            if dp2[i] != -1:
                dp2[i + 1] = max(dp2[i] + zero * tmp, dp2[i] + one * tmp)

    print((max(dp1[max_len], dp2[max_len])))


def __starting_point():
    main()


__starting_point()
