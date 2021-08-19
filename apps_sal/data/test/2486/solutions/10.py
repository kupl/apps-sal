def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    from itertools import combinations, permutations
    from bisect import bisect_left, bisect_right
    from math import floor, ceil
    import numpy as np
    (N, K) = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    def check(num):
        dp = np.zeros((N + 1, K), dtype=np.bool)
        dp[0, 0] = 1
        for i in range(N):
            dp[i + 1] |= dp[i]
            if i != num and a[i] < K:
                dp[i + 1, a[i]:] |= dp[i, :K - a[i]]
        return any(dp[N, -a[num]:])
    left = -1
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    print(right)


def __starting_point():
    main()


__starting_point()
