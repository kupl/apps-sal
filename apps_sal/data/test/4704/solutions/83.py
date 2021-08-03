

#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline
INF = pow(10, 10)
# @njit


def solve(n, a):
    res = INF
    x = 0
    y = sum(a)
    for i in range(n - 1):
        x += a[i]
        y -= a[i]
        res = min(res, abs(x - y))
    return res


def main():
    N = int(input())
    # N,M = map(int,input().split())
    a = list(map(int, input().split()))
    print((solve(N, a)))
    return


def __starting_point():
    main()


__starting_point()
