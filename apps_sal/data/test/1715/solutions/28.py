#!/usr/bin/env python3
import bisect

INF = 10 ** 18


def solve(s, t, x):
    ans = [0] * len(x)
    for i in range(len(x)):
        b = bisect.bisect_right(s, x[i])
        d = bisect.bisect_right(t, x[i])
        res = INF
        for S in [s[b - 1], s[b]]:
            for T in [t[d - 1], t[d]]:
                res = min(res, abs(S - x[i]) + abs(T - S), abs(T - x[i]) + abs(T - S))
        ans[i] = res
    return ans


def main():
    A, B, Q = list(map(int, input().split()))
    s = [-10**18] + [int(input()) for _ in range(A)] + [10**18]
    t = [-10**18] + [int(input()) for _ in range(B)] + [10**18]
    x = [int(input()) for _ in range(Q)]
    ans = solve(s, t, x)
    for i in range(Q):
        print((ans[i]))
    return


def __starting_point():
    main()


__starting_point()
