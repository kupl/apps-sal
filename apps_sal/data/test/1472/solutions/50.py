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
    (n, x, y) = i_map()
    ans = [0] * n
    for fr in range(1, n + 1):
        for to in range(fr + 1, n + 1):
            cost = min(to - fr, abs(x - fr) + abs(to - y) + 1)
            ans[cost] += 1
    print(*ans[1:], sep='\n')


def __starting_point():
    main()


__starting_point()
