def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    mod = 10 ** 9 + 7
    max_n = 2 * 10 ** 5
    (fac, inv) = ([1] * (max_n + 1), [0] * (max_n + 1))
    for i in range(2, max_n + 1):
        fac[i] = fac[i - 1] * i % mod
    inv[-1] = pow(fac[-1], mod - 2, mod)
    for i in range(max_n, 0, -1):
        inv[i - 1] = inv[i] * i % mod

    def ncr(n, r):
        return fac[n] * inv[r] * inv[n - r] % mod
    (n, k) = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if i > k:
            continue
        res += ncr(n, i) * ncr(n - 1, i)
        res %= mod
    print(res)


def __starting_point():
    main()


__starting_point()
