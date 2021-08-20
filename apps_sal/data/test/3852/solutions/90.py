import sys
import queue
import math
import copy
import itertools
import bisect
import collections
import heapq


def main():
    sys.setrecursionlimit(10 ** 7)
    INF = 10 ** 7
    MOD = 10 ** 9 + 7

    def LI():
        return [int(x) for x in sys.stdin.readline().split()]

    def NI():
        return int(sys.stdin.readline())

    def SI():
        return sys.stdin.readline().rstrip()
    N = NI()
    A = LI()
    ans = []
    max_a = max(A)
    min_a = min(A)
    if max_a * min_a < 0:
        p = max_a if abs(max_a) > abs(min_a) else min_a
        q = A.index(p)
        for i in range(N):
            ans.append((q + 1, i + 1))
            A[i] += p
        min_a = min(A)
    if min_a >= 0:
        for i in range(1, N):
            ans.append((i, i + 1))
    else:
        for i in range(N, 1, -1):
            ans.append((i, i - 1))
    print(len(ans))
    for x in ans:
        print(x[0], x[1])


def __starting_point():
    main()


__starting_point()
