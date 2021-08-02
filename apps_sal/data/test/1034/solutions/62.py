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
    X, Y, Z, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    q = []
    heappush(q, (-(A[0] + B[0] + C[0]), 0, 0, 0))
    count = 0
    used = set()

    while count < K:
        num, s, t, u = heappop(q)
        print((-num))
        used.add((s, t, u))

        if s + 1 < X and (s + 1, t, u) not in used:
            heappush(q, (-(A[s + 1] + B[t] + C[u]), s + 1, t, u))
            used.add((s + 1, t, u))
        if t + 1 < Y and (s, t + 1, u) not in used:
            heappush(q, (-(A[s] + B[t + 1] + C[u]), s, t + 1, u))
            used.add((s, t + 1, u))
        if u + 1 < Z and (s, t, u + 1) not in used:
            heappush(q, (-(A[s] + B[t] + C[u + 1]), s, t, u + 1))
            used.add((s, t, u + 1))
        count += 1


def __starting_point():
    main()


__starting_point()
