from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate


def main():
    N, M, Q = list(map(int, input().split()))
    ans = [[0] * N for _ in range(N)]
    for i in range(M):
        L, R = [int(x) - 1 for x in input().split()]
        ans[L][R] += 1

    for i in range(N):
        if i != N - 1:
            for j in range(N):
                ans[N - 2 - i][j] += ans[N - 1 - i][j]
        for j in range(N - 1):
            ans[N - 1 - i][j + 1] += ans[N - 1 - i][j]
    for i in range(Q):
        p, q = list(map(int, input().split()))
        print((ans[p - 1][q - 1]))


def __starting_point():
    main()


__starting_point()
