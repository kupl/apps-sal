import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
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


def S(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


def slv(K):
    ans = [(i, i / S(i)) for i in range(1, 10)]
    for i in range(16):
        a = i
        if a > 4:
            a = 4
        for j in range(1, 10 ** a):
            b = 10 ** (i - a + 1) * j + (10 ** (i - a + 1) - 1)
            if b < 10 ** (i - 1):
                continue
            s = S(b)
            while ans[-1][1] > b / s or ans[-1][0] == b:
                ans.pop()
            ans.append((b, b / s))
    error_print(len(ans))
    return '\n'.join(map(str, map(lambda x: x[0], ans[:K])))


def main():
    K = read_int()
    print(slv(K))


def __starting_point():
    main()


__starting_point()
