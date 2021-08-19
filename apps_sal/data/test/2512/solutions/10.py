from numba import njit, i8
import numpy as np
import sys
from decimal import Decimal
import math
from itertools import combinations, product
import bisect
from collections import Counter, deque, defaultdict
MOD = 10 ** 6 + 7
INF = 10 ** 9
PI = 3.141592653589793


def read_str():
    return sys.stdin.readline().strip()


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    return map(int, sys.stdin.readline().strip().split())


def read_str_list():
    return list(sys.stdin.readline().strip().split())


def read_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


@njit(i8(i8, i8, i8[:, :]))
def dp(R, C, grid):
    dp = np.zeros((R + 1, C + 1, 4), np.int64)
    for y in range(1, R + 1):
        for x in range(1, C + 1):
            for i in range(4):
                dp[y][x][i] = max(dp[y][x - 1][i], dp[y - 1][x][3])
            for i in range(3, 0, -1):
                dp[y][x][i] = max(dp[y][x][i], dp[y][x][i - 1] + grid[y - 1][x - 1])
    return dp[R][C][3]


def Main():
    (R, C, k) = read_ints()
    item = [read_int_list() for _ in range(k)]
    grid = np.zeros((R, C), np.int64)
    for (r, c, v) in item:
        grid[r - 1][c - 1] = v
    print(dp(R, C, grid))


if __name__ == '__main__':
    Main()
