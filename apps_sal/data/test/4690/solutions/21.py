#!/usr/bin/env python3

def main():
    a, b, c, d = list(map(int, input().split()))
    print((max(a * b, c * d)))


def __starting_point():
    main()

__starting_point()
