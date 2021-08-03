#!/usr/bin/env python3
from bisect import bisect_right
# input = stdin.readline


def solve(n, k, a):
    def calcCumSum(a):
        l = [0] * (len(a) + 1)
        for i in range(len(a)):
            l[i + 1] = l[i] + a[i]
        return l

    cum = calcCumSum(a)

    def calcSectionSum(cum, left, right):
        return cum[right] - cum[left]

    res = 0
    for left in range(n):
        ng, ok = left, n + 1
        while abs(ng - ok) > 1:
            mid = (ng + ok) // 2
            if calcSectionSum(cum, left, mid) >= k:
                ok = mid
            else:
                ng = mid
        res += n - ok + 1
    return res


def main():
    N, K = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print((solve(N, K, a)))
    return


def __starting_point():
    main()


__starting_point()
