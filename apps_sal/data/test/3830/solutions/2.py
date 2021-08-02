import sys
import random
# import numpy as np
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

# sys.setrecursionlimit(1000000)
# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")

MOD = 10 ** 9 + 7
divide = lambda x: pow(x, MOD - 2, MOD)


def solve():
    n = getN()
    S = getS()

    if "<" not in S:
        print(n)
        return
    if ">" not in S:
        print(n)
        return

    S = S + S[0]
    ans = 0
    for i in range(n):
        if S[i] == "-" or S[i + 1] == "-":
            ans += 1

    print(ans)


def main():
    n = getN()
    for _ in range(n):
        solve()

    return


def __starting_point():
    main()
    # solve()


__starting_point()
