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
    return tuple(map(int, input().split()))


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
def slv(N, XY):
    g = [[] for _ in range((10**5) * 2)]
    offset = 10**5
    cs = set()
    for x, y in XY:
        x -= 1
        y = y - 1 + offset
        g[x].append(y)
        g[y].append(x)
        cs.add(x)
        cs.add(y)
    ans = 0
    while cs:
        error_print(len(cs))
        q = set([cs.pop()])
        done = set()
        done_c = set()
        while q:
            v = q.pop()
            for u in g[v]:
                if v >= offset:
                    e = (u, v)
                else:
                    e = (v, u)
                if e not in done:
                    q.add(u)
                    done.add(e)
                    done_c.add(u)
                    done_c.add(v)
        xn = set()
        yn = set()
        for v, u in done:
            for z in (v, u):
                if z >= offset:
                    yn.add(z)
                else:
                    xn.add(z)
        ans += (len(xn) * len(yn)) - len(done)
        cs -= done_c

    return ans


def main():
    N = read_int()
    XY = [read_int_n() for _ in range(N)]
    print(slv(N, XY))


def __starting_point():
    main()


__starting_point()
