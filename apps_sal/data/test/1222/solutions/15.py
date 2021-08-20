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
    k = i_input()
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for _ in range(k):
        ans = x = q.popleft()
        x0 = x % 10
        if x0 >= 1:
            q.append(x * 10 + x0 - 1)
        q.append(x * 10 + x0)
        if x0 <= 8:
            q.append(x * 10 + x0 + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
