from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float('inf')
sys.setrecursionlimit(10 ** 6)


def i_input():
    return int(input())


def i_map():
    return list(map(int, input().split()))


def i_list():
    return list(i_map())


def i_row(N):
    return [i_input() for _ in range(N)]


def i_row_list(N):
    return [i_list() for _ in range(N)]


def s_input():
    return input()


def s_map():
    return input().split()


def s_list():
    return list(s_map())


def s_row(N):
    return [s_input for _ in range(N)]


def s_row_str(N):
    return [s_list() for _ in range(N)]


def s_row_list(N):
    return [list(s_input()) for _ in range(N)]


def main():
    (n, k) = i_map()
    x = i_list()
    l = []
    r = []
    for i in x:
        if i < 0:
            l.append(-i)
        else:
            r.append(i)
    l.reverse()
    R_len = len(r)
    L_len = len(l)
    ans = INF
    for (i, j) in enumerate(l):
        if R_len >= k - i - 1:
            if R_len == 0:
                ans = min(ans, j)
            else:
                ans = min(ans, 2 * j + r[k - i - 2])
    for (i, j) in enumerate(r):
        if L_len >= k - i - 1:
            if L_len == 0:
                ans = min(ans, j)
            else:
                ans = min(ans, 2 * j + l[k - i - 2])
    print(ans)


def __starting_point():
    main()


__starting_point()
