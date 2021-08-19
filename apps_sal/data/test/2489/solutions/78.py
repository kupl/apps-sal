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
    N = i_input()
    A = i_list()
    P = [True] * (10 ** 6 + 1)
    C = Counter(A)
    s = list(set(A))
    for x in s:
        t = x * 2
        while t <= 10 ** 6:
            P[t] = False
            t += x
    ans = 0
    for x in A:
        if C[x] == 1 and P[x] == True:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
