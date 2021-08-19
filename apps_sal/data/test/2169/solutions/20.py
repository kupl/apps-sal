#!/usr/bin/env python3
import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def main():
    H, W, D = list(map(int, input().split()))
    A = [None] * (H * W)
    for i in range(H):
        s = list(map(int, input().split()))
        for j in range(W):
            A[s[j] - 1] = (i, j)

    # print(A)
    costs = [0] * (H * W)
    for i in range(D):
        j = H * W - 1 - i
        while j - D >= 0:
            costs[j - D] = costs[j] + abs(A[j][0] - A[j - D][0]) + abs(A[j][1] - A[j - D][1])
            j -= D

    Q = int(input())
    for i in range(Q):
        L, R = [int(x) - 1 for x in input().split()]
        print((costs[L] - costs[R]))


def __starting_point():
    main()


__starting_point()
