from heapq import heappop, heappush
import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def Main():
    n, q = read_ints()
    num = 2 * (10 ** 5)
    kindergarten = [[] for _ in range(num)]
    rating = [0] * n
    now = [0] * n

    for i in range(n):
        a, b = read_ints()
        heappush(kindergarten[~-b], (-a, i))
        rating[i] = a
        now[i] = ~-b

    ranking = []
    for j in range(num):
        if kindergarten[j]:
            a, i = kindergarten[j][0]
            heappush(ranking, (-a, i))

    for _ in range(q):
        c, d = read_ints()
        last = now[~-c]
        now[~-c] = ~-d
        heappush(kindergarten[~-d], (-rating[~-c], ~-c))

        while kindergarten[last] and now[kindergarten[last][0][1]] != last:
            heappop(kindergarten[last])
        while kindergarten[~-d] and now[kindergarten[~-d][0][1]] != ~-d:
            heappop(kindergarten[~-d])

        if kindergarten[last]:
            a, i = kindergarten[last][0]
            heappush(ranking, (-a, i))
        if kindergarten[~-d]:
            a, i = kindergarten[~-d][0]
            heappush(ranking, (-a, i))

        while ranking and kindergarten[now[ranking[0][1]]][0][1] != ranking[0][1]:
            heappop(ranking)

        print(ranking[0][0])


def __starting_point():
    Main()


__starting_point()
