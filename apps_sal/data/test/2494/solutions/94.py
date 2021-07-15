# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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
def slv(K):

    g = defaultdict(dict)
    for i in range(1, K+1):
        g[i % K][(i+1) % K] = 1
        g[i % K][(i*10) % K] = 0

    q = deque()
    q.append((1, 0))

    vis = {}
    while q:
        u, cc = q.popleft()
        if u == 0:
            return cc + 1
        vis[u] = True
        for v, c in g[u].items():
            if v in vis:
                continue
            if c == 0:
                q.appendleft((v, cc))
            else:
                q.append((v, cc+c))


def main():
    K = read_int()
    print(slv(K))


def __starting_point():
    main()

__starting_point()
