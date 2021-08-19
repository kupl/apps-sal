from functools import reduce, lru_cache     # decorator: 関数をメモ化再起してくれる. max_size=128
from pprint import pprint
from collections import deque, defaultdict
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
from math import ceil, floor, log2, log, sqrt, gcd
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return list(map(int, input().split()))
def MI1(): return list(map(int1, input().split()))
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return input().strip('\n')
def MS(): return input().split()
def LS(): return list(input().strip('\n'))
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def gen_matrix(h, w, init): return [[init] * w for _ in range(h)]


INF = float('inf')
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum


def solve():
    N = II()
    S = LLS(2)
    MOD = 1_000_000_007

    i = 0
    pre = 'N'
    ans = 1
    while i < N:
        s, t = S[0][i], S[1][i]
        if s == t:
            tp = 'H'
            i += 1
        else:
            tp = 'V'
            i += 2

        if pre == 'N':
            if tp == 'H':
                ans = 3
            else:
                ans = 6
        else:
            p = [pre, tp]
            if p == ['H', 'H']:
                ans = ans * 2 % MOD
            elif p == ['H', 'V']:
                ans = ans * 2 % MOD
            elif p == ['V', 'H']:
                pass
            elif p == ['V', 'V']:
                ans = ans * 3 % MOD
        pre = tp
    print(ans)


def __starting_point():
    solve()


__starting_point()
