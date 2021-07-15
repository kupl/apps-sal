from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from heapq import heappop, heappush
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def main():
    K = int(input())
    dp = [INF] * K
    dp[1] = 1

    heap = []
    heappush(heap, (1, 1))

    while len(heap) != 0:
        k, p = heappop(heap)
        if dp[(p + 1) % K] > dp[p] + 1:
            dp[(p + 1) % K] = dp[p] + 1
            heappush(heap, (dp[p] + 1, (p + 1) % K))
        if dp[(p * 10) % K] > dp[p]:
            dp[(p * 10) % K] = dp[p]
            heappush(heap, (dp[p], (p * 10) % K))

        if dp[0] != INF:
            break

    print((dp[0]))


def __starting_point():
    main()

__starting_point()
