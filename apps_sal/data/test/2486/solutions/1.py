"""
1枚抜いてDPをN枚についてやれば良い, がこれでは間に合わない
そこで必要不要の境界を二分探索で探す
するとO(N^2K)→O(NKlogN)となって間に合う

もう1つの方法は分からない
"""


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    from itertools import combinations, permutations
    from bisect import bisect_left, bisect_right
    from math import floor, ceil
    (N, K) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = sorted(a)
    a = a[:bisect_left(a, K)]
    n = len(a)
    import numpy as np

    def dp(omit):
        dp = np.zeros((n + 1, K), dtype=np.bool)
        dp[0, 0] = 1
        for i in range(n):
            dp[i + 1] |= dp[i]
            if i != omit and a[i] < K:
                dp[i + 1, a[i]:] |= dp[i, :K - a[i]]
        for j in range(max(0, K - a[omit]), K):
            if dp[n, j]:
                return True
        return False
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if dp(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(right + 1)


def __starting_point():
    main()


__starting_point()
