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
    N, M = list(map(int, input().split()))
    xyz = [None for _ in range(N)]
    for i in range(N):
        xyz[i] = list(map(int, input().split()))
    # print(xyz)
    ans = 0
    for i in range(2**3):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if i >> k & 1:
                    tmp[j] += xyz[j][k]
                else:
                    tmp[j] -= xyz[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

def __starting_point():
    main()

__starting_point()
