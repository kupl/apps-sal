#!/usr/bin/env python3
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(500000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def calc(p, P):
    ans = 0
    for i in range(1, len(p)):
        x1, y1 = P[p[i - 1]]
        x2, y2 = P[p[i]]
        ans += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return ans


def solve():
    N = int(input())
    P = []
    for _ in range(N):
        X, Y = list(map(int, input().split()))
        P.append((X, Y))

    ans = 0
    num = 0
    for p in permutations(list(range(N))):
        ans += calc(p, P)
        num += 1
    print((ans / num))


def main():
    solve()


def __starting_point():
    main()


__starting_point()
