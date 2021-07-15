#!/usr/bin/env python3
# coding: utf-8
import collections
import math
def debug(arg):
    if __debug__:
        pass
    else:
        import sys
        print(arg, file=sys.stderr)

def main():
    pass
    N, *A = map(int, open(0).read().split())
    a = dict(enumerate(A, 1))
    dp = collections.defaultdict(lambda: -float("inf"))
    dp[0, 0] = 0 
    dp[1, 0] = 0 
    dp[1, 1] = a[1]
    for i in range(2, N + 1):
        jj = range(max(math.floor(i // 2 - 1), 1), math.ceil((i + 1) // 2) + 1)
        for j in jj:
            x = dp[i - 2, j - 1] + a[i]
            y = dp[i - 1, j]
            dp[i, j] = max(x, y)
    print(dp[N, N // 2])

def __starting_point():
    main()
__starting_point()
