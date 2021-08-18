from collections import defaultdict, deque
import sys
from bisect import bisect_left
import copy
import math


def getN():
    return int(input())


def getNM():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


INF = 10 ** 17
MOD = 998244353


def solve():
    n = getN()
    ans = 0
    radius = n // 2
    for r in range(radius):
        ra = r + 1
        ans += ra * ((ra * 2 + 1) ** 2 - (ra * 2 - 1) ** 2)
    print(ans)


def main():
    n = getN()
    for _ in range(n):
        solve()


def __starting_point():
    main()


__starting_point()
