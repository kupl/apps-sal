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
    n = i_input()
    l = [i_list() for i in range(n)]
    L = []
    for i in l:
        if i[2] != 0:
            L.append(i)
    if len(L) == 1:
        print(' '.join(map(str, L[0])))
        return
    for x in range(101):
        for y in range(101):
            H = L[0][2] + abs(x - L[0][0]) + abs(y - L[0][1])
            flg = True
            for (x1, y1, h1) in L[1:]:
                if h1 == 0:
                    pass
                if H != h1 + abs(x - x1) + abs(y - y1):
                    flg = False
                    break
            if flg == True:
                ans = [x, y]
    H = L[0][2] + abs(ans[0] - L[0][0]) + abs(ans[1] - L[0][1])
    print(' '.join(map(str, ans)) + ' ' + str(H))


def __starting_point():
    main()


__starting_point()
