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
    N, K = list(map(int, input().split()))
    V = list(map(int, input().split()))

    # 方針: 操作Aの回数・操作Bの回数で全探索
    ans = 0
    R = min(N, K)

    for i in range(R + 1):
        for j in range(R + 1 - i):
            tmp = 0
            q = []  # 価値が負の宝石をいれる(C)

            for k in range(i):
                tmp += V[k]
                if V[k] < 0:
                    q.append(V[k])
            for k in range(j):
                tmp += V[N - 1 - k]
                if V[N - 1 - k] < 0:
                    q.append(V[N - 1 - k])

            q.sort()
            tmp -= sum(q[:min(len(q), K - i - j)])
            ans = max(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
