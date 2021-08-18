import string
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
    N, H = i_map()
    l = []
    for _ in range(N):
        a, b = i_map()
        l.append([a, b])
    t = [list(i) for i in zip(*l)]
    ans = 0

    M = max(t[0])
    throw = 0
    for i in sorted(t[1], reverse=True):
        if i > M:
            throw += i
            H -= i
            ans += 1
            if H <= 0:
                print(ans)
                return
    i = t[0].index(M)
    if H % M == 0:
        ans += H // M
    else:
        ans += H // M + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
