def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    mod = 10**9 + 7

    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    res = 0
    b = pow(2, n, mod)
    for i in range(n):
        l = pow(2, i, mod)
        if n - i - 2 >= 0:
            r = pow(2, n - i - 1, mod) + (n - i - 1) * pow(2, n - i - 2, mod)
        else:
            r = pow(2, n - i - 1, mod)
        res += b * c[i] * l * r % mod
        res %= mod
    print(res)


def __starting_point():
    main()


__starting_point()
