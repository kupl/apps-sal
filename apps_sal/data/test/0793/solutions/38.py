import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()
        error_print(e - s, 'sec')
        return ret
    return wrap


@mt
def slv(N, M, S, T):
    MOD = 10 ** 9 + 7
    dp0 = [1] * (M + 1)
    for s in S:
        dp1 = dp0[:]
        k = 0
        for (j, t) in enumerate(T):
            if s == t:
                k += dp0[j]
            dp1[j + 1] = (dp0[j + 1] + k) % MOD
        dp0 = dp1
    return dp0[-1]


def main():
    (N, M) = read_int_n()
    S = read_int_n()
    T = read_int_n()
    print(slv(N, M, S, T))


def __starting_point():
    main()


__starting_point()
