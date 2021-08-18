import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache, reduce
from operator import xor
from heapq import heappush, heappop
INF = float("inf")
sys.setrecursionlimit(10**7)

dy4, dx4 = [0, -1, 0, 1], [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def ceil(a, b): return (a + b - 1) // b


YES = "Yes"
NO = "No"


def check(x, nums):
    x = abs(x)
    dp = [False] * (x + 1)
    dp[0] = True
    for y in nums:
        tmp = [False] * (x + 1)
        for i in range(len(dp)):
            if i + y < len(tmp):
                tmp[i + y] |= dp[i]
            if i - y >= 0:
                tmp[i - y] |= dp[i]
        dp = tmp
    return dp[x]


def solve(s, x, y):
    type_num = [(k, len(list(g))) for k, g in groupby(s)]
    if s[0] == "F":
        x -= type_num[0][1]
        type_num.pop(0)

    h, v = [], []
    now = 0
    for t, n in type_num:
        if t == "F":
            if now == 0:
                h.append(n)
            else:
                v.append(n)
        else:
            if n % 2 != 0:
                now = (now + 1) % 2
    return YES if check(x, h) and check(y, v) else NO


def main():
    s = input()
    x, y = list(map(int, input().split()))

    print((solve(s, x, y)))


def __starting_point():
    main()


__starting_point()
