import math
from math import gcd,pi,sqrt
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

import string

def main():
    N = i_input()
    k = len(str(N))
    ans = 0
    l = []
    def rec(n,k):
        k += 1
        if int(n) > N:
            return
        if "3" in n and "5" in n and "7" in n:
            l.append(int(n))
        rec(n+"3",k)
        rec(n+"5",k)
        rec(n+"7",k)
    rec("0",0)
    print((len(l)))





def __starting_point():
    main()

__starting_point()
