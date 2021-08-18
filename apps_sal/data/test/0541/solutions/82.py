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
    ab = []
    for _ in range(M):
        a, b = [int(x) - 1 for x in input().split()]
        ab.append((b, a))
    ab.sort()
    ans = 0
    x = -1
    for i in range(M):
        if ab[i][1] > x:
            ans += 1
            x = ab[i][0] - 1
    print(ans)


def __starting_point():
    main()


__starting_point()
