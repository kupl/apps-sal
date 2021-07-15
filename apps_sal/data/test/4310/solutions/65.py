#!/usr/bin/env python3

def main():
    *a, = list(map(int, input().split()))
    print((max(a) - min(a)))


def __starting_point():
    main()

__starting_point()
