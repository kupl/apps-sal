from collections import Counter, deque
import bisect
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")
MOD = 10**9 + 7

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n = i_input()
    a = i_list()
    ans = 0

    for i in range(60):
        cnt = 0
        bit = 1 << i
        for j in a:
            if j & bit:
                cnt += 1
        num1 = cnt
        num0 = n - num1
        ans += ((num1 * num0) * bit) % MOD
    print((ans % MOD))


def __starting_point():
    main()


__starting_point()
