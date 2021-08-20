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
    (N, M) = i_map()
    K = []
    for i in range(M):
        l = i_list()
        l.pop(0)
        K.append(l)
    P = i_list()
    cnt = 0
    for i in range(2 ** N):
        trial = []
        for j in range(N):
            if i >> j & 1:
                trial.append(1)
            else:
                trial.append(0)
        flg = True
        for (h, g) in enumerate(K):
            num = 0
            for r in g:
                if trial[r - 1] == 1:
                    num += 1
            if num % 2 != P[h]:
                flg = False
        if flg == True:
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
