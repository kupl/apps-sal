# -*- coding: utf-8 -*-
import bisect
import heapq
import math
# import random
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


# @mt
def slv(N, AB):

    memo = [0, AB[0][1], AB[0][1] * 2]

    for i in range(1, N):
        a, b = AB[i]
        a1, _ = AB[i - 1]
        memo2 = [0] * 3
        for j in range(3):
            tmp = 1e+1000
            for k in range(3):
                if a + j != a1 + k:
                    tmp = min(tmp, memo[k])
            memo2[j] = tmp + j * b
        memo = memo2
    return min(memo)


def main():
    Q = read_int()
    for _ in range(Q):
        N = read_int()
        AB = [read_int_n() for _ in range(N)]
        print(slv(N, AB))

    # N = 100
    # AB = [[1000000000, 1000000000] for _ in range(N)]
    # print(slv(N, AB))


def __starting_point():
    main()


__starting_point()
