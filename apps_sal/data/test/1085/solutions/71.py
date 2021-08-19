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


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


# ===CODE===
# 約数を列挙　n=10^12までいける
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    divisors.remove(1)
    return divisors


def main():
    n = ni()

    ans = set()
    ans.add(n)
    for i in range(2, int(n ** (0.5)) + 1):
        tmp = n
        while tmp % i == 0:
            tmp //= i
        if (tmp - 1) % i == 0:
            ans.add(i)

    yaku = set(make_divisors(n - 1))

    ans = ans | yaku

    print((len(ans)))


def __starting_point():
    main()


__starting_point()
