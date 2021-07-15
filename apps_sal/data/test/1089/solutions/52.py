def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    mod = 10**9 + 7

    # max_nCrまで調べられる
    max_n = 4*10**5
    fac, inv = [1]*(max_n+1), [0]*(max_n+1)
    for i in range(2, max_n+1):
        fac[i] = fac[i-1] * i % mod
    inv[-1] = pow(fac[-1], mod-2, mod)
    for i in range(max_n, 0, -1):
        inv[i-1] = inv[i] * i % mod
    
    # nCrを求める
    def ncr(n, r):
        return fac[n]*inv[r]*inv[n-r]%mod

    n,m,k = map(int, input().split())

    base = ncr(n*m-2, k-2)

    res = 0
    # x方向
    for i in range(1, m):
        res += n**2 * i * (m-i)
        res %= mod

    for i in range(1, n):
        res += m**2 * i * (n-i)
        res %= mod

    print(res*base%mod)

def __starting_point():
    main()
__starting_point()
