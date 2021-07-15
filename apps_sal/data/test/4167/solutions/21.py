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

def main():
    n,k = i_map()

    R = [0]*k
    for i in range(1,n+1):
        R[i%k] += 1

    ans = 0
    for a in range(k):
        b = (k-a)%k
        if 2*b%k == 0: # b==cとしてbを2倍
            ans += R[a] * R[b] * R[b]

    print(ans)

def __starting_point():
    main()

__starting_point()
