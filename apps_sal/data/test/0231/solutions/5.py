#!/usr/bin/env python


def main():
    n, a = [int(x) for x in input().split()]
    if a % 2 == 0:
        print(n // 2 - a // 2 + 1)
    else:
        print(a // 2 + 1)


def __starting_point():
    main()


__starting_point()
