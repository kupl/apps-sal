import os
import sys
import math
from _thread import start_new_thread
from bisect import bisect_right


class pair:

    def __init__(self, a):
        (self.first, self.second) = (a[0], a[1])


def main():
    INF = 10 ** 18
    n = int(input())
    c = list(map(int, input().split()))
    (a, b) = ([], [])
    for i in range(n):
        s = input()
        a.append(s)
        b.append(s[::-1])
    dp = [pair([INF, INF]) for i in range(0, n)]
    (dp[0].first, dp[0].second) = (0, c[0])
    for i in range(1, n):
        dp[i].first = INF
        dp[i].second = INF
        if a[i] >= a[i - 1]:
            dp[i].first = min(dp[i].first, dp[i - 1].first)
        if a[i] >= b[i - 1]:
            dp[i].first = min(dp[i].first, dp[i - 1].second)
        if b[i] >= a[i - 1]:
            dp[i].second = min(dp[i].second, dp[i - 1].first + c[i])
        if b[i] >= b[i - 1]:
            dp[i].second = min(dp[i].second, dp[i - 1].second + c[i])
    res = min(dp[n - 1].first, dp[n - 1].second)
    print([-1, res][res != INF])


def __starting_point():
    return int(main() or 0)


__starting_point()
