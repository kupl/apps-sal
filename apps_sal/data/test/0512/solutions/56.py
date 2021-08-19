import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter
import sys
readline = sys.stdin.readline
INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()
        ep(e - s, 'sec')
        return ret
    return wrap


@mt
def slv(N, AB):
    used = set()
    for (a, b) in AB:
        if a > 0 and b > 0 and (a >= b):
            return 'No'
        if a > 0 and a in used:
            return 'No'
        else:
            used.add(a)
        if b > 0 and b in used:
            return 'No'
        else:
            used.add(b)
    AB = [(a - 1, b - 1) for (a, b) in AB]

    @lru_cache(maxsize=None)
    def f(s):
        if s == 2 * N:
            return True
        for r in range(s + 2, 2 * N + 1, 2):
            l = r - s
            l2 = l // 2
            r2 = s + l2
            used = Counter()
            for (a, b) in AB:
                if a >= 0 and r2 <= a < r:
                    break
                if b >= 0 and s <= b < r2:
                    break
                if s <= a < r2 and r2 <= b < r and (b - a != l2):
                    break
                if s <= a < r2:
                    used[a] += 1
                    if b < 0:
                        used[a + l2] += 1
                if r2 <= b < r:
                    used[b] += 1
                    if a < 0:
                        used[b - l2] += 1
            else:
                if used and used.most_common()[0][1] > 1:
                    pass
                elif f(r):
                    ep(s, True)
                    return True
        ep(s, False)
        return False
    return 'Yes' if f(0) else 'No'


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, AB))


def __starting_point():
    main()


__starting_point()
