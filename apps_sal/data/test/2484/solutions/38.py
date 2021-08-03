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
    N = int(input())
    A = list(map(int, input().split()))

    # しゃくとり法の練習
    res = 0
    right = 0
    sumA = 0  # leftからrightまでの算術和（=論理和）

    for left in range(N):
        while right < N and (sumA + A[right]) == sumA ^ A[right]:
            sumA += A[right]
            right += 1

        res += right - left
        if left == right:
            right += 1
        else:
            sumA -= A[left]

    print(res)


def __starting_point():
    main()


__starting_point()
