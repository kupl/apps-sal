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
    (L, R) = i_map()
    ans = 2018
    for i in range(L, min(R + 1, L + 2030)):
        for j in range(L + 1, min(R + 1, L + 2030)):
            if i != j:
                ans = min(ans, i * j % 2019)
    print(ans)


def __starting_point():
    main()


__starting_point()
