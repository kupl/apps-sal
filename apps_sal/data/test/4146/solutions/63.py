#!/usr/bin/env python3
from collections import Counter
# from numba import njit

# input = stdin.readline

# @njit


def solve(n, v):
    if all(x == v[0] for x in v):
        return n // 2
    v_even = v[::2]
    v_odd = v[1::2]

    d_even = list(sorted(list(Counter(v_even).items()), key=lambda x: x[1], reverse=True))
    d_odd = list(sorted(list(Counter(v_odd).items()), key=lambda x: x[1], reverse=True))
    e0 = d_even[0]
    o0 = d_odd[0]
    if e0[0] != o0[0]:
        return n - e0[1] - o0[1]
    e1 = d_even[1]
    o1 = d_odd[1]
    return min(n - e0[1] - o1[1], n - e1[1] - o0[1])


def main():
    N = int(input())
    # N,M = map(int,input().split())
    v = list(map(int, input().split()))
    print((solve(N, v)))
    return


def __starting_point():
    main()


__starting_point()
