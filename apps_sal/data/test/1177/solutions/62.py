import math
import numpy as np
import queue
from collections import deque, defaultdict
import heapq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)


def main():
    n, s = list(map(int, ipt().split()))
    a = [int(i) for i in ipt().split()]
    mod = 998244353
    ans = 0
    dp = np.zeros(s + 1, dtype=int)
    for j in range(n):
        dp[0] += 1
        aj = a[j]
        ndp = dp * 1
        if s >= aj:
            dp[s - aj] *= (n - j)
        ndp[aj:] += dp[:-aj]
        ndp %= mod
        dp = ndp
    print((dp[s]))
    return


def __starting_point():
    main()


__starting_point()
