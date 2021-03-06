def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    inf = 10 ** 17
    (N, W) = map(int, input().split())
    dp = [[inf] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    abc = [list(map(int, input().split())) for _ in range(W)]
    for (a, b, c) in abc:
        dp[a - 1][b - 1] = c
        dp[b - 1][a - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] == inf or dp[k][j] == inf:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    res = 0
    for (a, b, c) in abc:
        for k in range(N):
            if dp[a - 1][k] == c + dp[b - 1][k]:
                res += 1
                break
    print(W - res)


def __starting_point():
    main()


__starting_point()
