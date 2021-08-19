from collections import Counter, deque
import bisect
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float('inf')
MOD = 10 ** 9 + 7
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
    (N, X) = i_map()
    (a, p) = ([1], [1])
    for i in range(N):
        a.append(a[i] * 2 + 3)
        p.append(p[i] * 2 + 1)

    def f(N, X):
        if N == 0:
            return 0 if X <= 0 else 1
        elif X <= 1 + a[N - 1]:
            return f(N - 1, X - 1)
        else:
            return p[N - 1] + 1 + f(N - 1, X - 2 - a[N - 1])
    print(f(N, X))


def __starting_point():
    main()


__starting_point()
