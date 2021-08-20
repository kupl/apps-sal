import math
from collections import defaultdict
import sys
input = sys.stdin.readline


def main():
    (n, m, k) = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    pref = [0] + a.copy()
    for i in range(1, n + 1):
        pref[i] += pref[i - 1]

    def getPref(start, end):
        if start > end:
            return 0
        if start == 0:
            return pref[end]
        return pref[end] - pref[start - 1]
    offers = {}
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        if a not in offers:
            offers[a] = b
        elif b > offers[a]:
            offers[a] = b
    if 1 not in offers:
        offers[1] = 0
    dp = [math.inf] * (k + 1)
    dp[0] = 0
    for i in range(0, k + 1):
        for j in offers:
            if i + j <= k:
                dp[i + j] = min(dp[i + j], dp[i] + getPref(i + offers[j] + 1, i + j))
    print(dp[k])


def __starting_point():
    main()


__starting_point()
