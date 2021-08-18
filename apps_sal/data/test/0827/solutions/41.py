import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate
from itertools import product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = float('inf')
num_list = []
str_list = []


def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]
def s_row_str(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)


def main():
    n = i_input()
    t = s_input()

    S = "110"

    ok = False
    for i in range(3):
        for j in range(len(t)):
            if t[j] != S[(j + i) % 3]:
                break
        else:
            ok = True

    if not ok:
        print((0))
        return
    else:
        if t == "1":
            print((2 * 10 ** 10))
        elif t == "11":
            print((10 ** 10))
        else:
            c = t.count("0")
            if t[-1] == "0":
                print((10**10 - c + 1))
            else:
                print((10**10 - c))


def __starting_point():
    main()


__starting_point()
