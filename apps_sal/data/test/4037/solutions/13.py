import math
import sys
from collections import defaultdict


def nt(): return map(int, input().split())


def main():
    n, r = nt()
    projects = [tuple(nt()) for _ in range(n)]
    positive = [t for t in projects if t[1] > 0]
    negative = [t for t in projects if t[1] <= 0]

    max_pos = 0
    for p in sorted(positive):
        if p[0] <= r:
            r += p[1]
            max_pos += 1
        else:
            break
    negative.sort(key=lambda x: -x[0] - x[1])
    MAX = 60001
    dp = [[-1 for _ in range(MAX)] for _ in range(len(negative) + 1)]
    dp[0][r] = 0
    for i in range(len(negative)):
        for j in range(MAX):
            if dp[i][j] == -1:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j >= negative[i][0] and j + negative[i][1] >= 0:
                dp[i + 1][j + negative[i][1]] = max(dp[i + 1][j + negative[i][1]], dp[i][j] + 1)
    max_neg = 0
    for i in range(MAX):
        max_neg = max(max_neg, dp[len(negative)][i])

    print(max_pos + max_neg)


def __starting_point():
    main()


__starting_point()
