import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    n = input()
    k = ni()

    l = len(n)

    dp_true = [[0 for _ in range(k + 2)] for i in range(l + 1)]
    dp_false = [[0 for i in range(k + 2)] for j in range(l + 1)]
    dp_false[0][0] = 1

    for i in range(l):
        num = int(n[i])

        for j in range(k + 1):
            dp_true[i + 1][j] += dp_true[i][j]
            dp_true[i + 1][j + 1] += dp_true[i][j] * 9

            if num > 0:
                dp_true[i + 1][j + 1] += dp_false[i][j] * (num - 1)
                dp_true[i + 1][j] += dp_false[i][j]

            if num > 0:
                dp_false[i + 1][j + 1] += dp_false[i][j]
            else:
                dp_false[i + 1][j] += dp_false[i][j]

    print((dp_true[l][k] + dp_false[l][k]))


def __starting_point():
    main()

__starting_point()
