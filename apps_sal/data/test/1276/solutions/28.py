import math
from math import gcd,pi
INF = float("inf")

import sys
sys.setrecursionlimit(10**6)
import itertools
from collections import Counter,deque
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
    s = s_input()

    r_cn = s.count("R")
    g_cn = s.count("G")
    b_cn = s.count("B")

    ans = r_cn*g_cn*b_cn

    for i in range(n):
        for d in range(n):
            j = i+d
            k = j+d
            if k >=n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)


def __starting_point():
    main()

__starting_point()
