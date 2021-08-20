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
    return map(int, input().split())


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
    M = i_input()
    B = [0] + i_list()
    N = [0] * (M + 1)
    for i in range(M, 0, -1):
        k = 2 * i
        trial = 0
        while k <= M:
            trial += N[k]
            k += i
        if trial % 2 == B[i]:
            continue
        else:
            N[i] = 1
    s = sum(N)
    print(s)
    if s > 0:
        for (i, k) in enumerate(N):
            if k > 0:
                print(i)


def __starting_point():
    main()


__starting_point()
