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
    h,w = i_map()
    n = i_input()

    a = i_list()
    ans = []
    for m,i in enumerate(a):
        ans.extend([str(m+1)]*i)
    ans = list(ans)
    for i in range(1,h+1):
        if i%2 == 0:
            print((" ".join(ans[w*(i-1):w*(i-1)+w])))
        else:
            print((" ".join(ans[w*(i-1):w*(i-1)+w][::-1])))

def __starting_point():
    main()

__starting_point()
