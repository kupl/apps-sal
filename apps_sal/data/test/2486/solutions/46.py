import bisect
import heapq
import math
import random
import sys
from pprint import pprint
from collections import Counter, defaultdict, deque
import queue
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

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
def slv(N, K, A):
    A.sort()

    s = 0
    ans = N
    for i in range(N - 1, -1, -1):
        if s + A[i] < K:
            s += A[i]
        else:
            ans = min(ans, i)
    return ans


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


def __starting_point():
    main()


__starting_point()
