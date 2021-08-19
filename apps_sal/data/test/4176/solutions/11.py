#!/usr/bin/env python3
def main():
    from math import gcd

    A, B = list(map(int, input().split()))

    print((A * B // gcd(A, B)))


def __starting_point():
    main()


__starting_point()
