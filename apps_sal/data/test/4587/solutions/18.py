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
    n = i_input()
    a = i_list()
    b = i_list()
    c = i_list()
    a.sort()
    b.sort()
    c.sort()

    al = []
    bl = [0]
    import bisect

    for k, i in enumerate(b):
        x = bisect.bisect(c, i)
        bl.append(bl[k] + (n - x))

    ans = 0

    for i in a:
        x = bisect.bisect(b, i)
        ans += bl[-1] - bl[x]
    print(ans)


def __starting_point():
    main()


__starting_point()
