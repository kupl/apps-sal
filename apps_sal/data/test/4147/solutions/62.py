from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")

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
    n, A, B, C = i_map()

    l = [i_input() for i in range(n)]

    def dfs(cur, a, b, c):
        if cur == n:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print((dfs(0, 0, 0, 0)))


def __starting_point():
    main()


__starting_point()
