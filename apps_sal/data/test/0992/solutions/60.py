import math
import numpy as np
import queue
from collections import deque, defaultdict
import heapq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)


def main():
    (n, s) = list(map(int, ipt().split()))
    a = [int(i) for i in ipt().split()]
    mod = 998244353
    two = [1] * (n + 1)
    for i in range(n):
        two[i + 1] = two[i] * 2 % mod
    dp = np.zeros(3010, dtype=int)
    dp[0] = 1
    for (i, ai) in enumerate(a):
        ndp = dp * 2
        ndp[ai:] += dp[:-ai]
        ndp %= mod
        dp = ndp
    print(dp[s])
    return


def __starting_point():
    main()


__starting_point()
