def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    h, w, k = map(int, input().split())
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1

    pattern = []
    if w > 2:
        for i in range(1 << (w - 1)):
            for j in range(w - 2):
                if ((i >> j) & 1) and ((i >> (j + 1)) & 1):
                    break
            else:
                pattern.append(i)
    else:
        print(1)
        return

    for i in range(h):
        for j in range(w):
            for p in pattern:
                if j == 0:
                    if p & 1:
                        dp[i + 1][j + 1] += dp[i][j] % mod
                    else:
                        dp[i + 1][j] += dp[i][j] % mod
                elif j == w - 1:
                    if (p >> (w - 2)) & 1:
                        dp[i + 1][j - 1] += dp[i][j] % mod
                    else:
                        dp[i + 1][j] += dp[i][j] % mod
                else:
                    if (p >> (j - 1)) & 1:
                        dp[i + 1][j - 1] += dp[i][j] % mod
                    elif (p >> j) & 1:
                        dp[i + 1][j + 1] += dp[i][j] % mod
                    else:
                        dp[i + 1][j] += dp[i][j] % mod
    print(dp[-1][k - 1] % mod)


def __starting_point():
    main()


__starting_point()
