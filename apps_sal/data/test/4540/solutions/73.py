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
    n = i_input()
    a = i_list()

    total = 0
    now = 0
    for i in a:
        total += abs(now-i)
        now = i
    total += abs(i)
    a.insert(0,0)
    a.append(0)

    ans = []

    for i,k in enumerate(a[1:-1], start=1):
        # print(i,k)

        if a[i-1] <= k and k <= a[i+1] or a[i-1] >= k and  k >= a[i+1]:
            ans.append(total)
        else:
            ans.append(total - abs(k-a[i-1]) - abs(k-a[i+1]) + abs(a[i-1]-a[i+1]))

    for i in ans:
        print(i)




def __starting_point():
    main()

__starting_point()
