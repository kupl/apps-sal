#!/usr/bin/env python3


def main():
    n, x = list(map(int, input().split()))
    left = abs(sum(map(int, input().split())))
    print("%s" % ((left - 1) // x + 1))


def __starting_point():
    main()


__starting_point()
