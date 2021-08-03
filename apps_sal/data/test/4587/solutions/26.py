#!/usr/bin/env python3
def main():
    from bisect import bisect, bisect_left

    N = int(input())
    A = sorted([int(x) for x in input().split()])
    B = [int(x) for x in input().split()]
    C = sorted([int(x) for x in input().split()])

    print((sum([bisect_left(A, b) * (N - bisect(C, b)) for b in B])))


def __starting_point():
    main()


__starting_point()
