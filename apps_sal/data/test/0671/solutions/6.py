#!/usr/bin/env python3


def main():
    n = int(input())
    print(''.join(map(str, list(range(0, 1000))))[n])


def __starting_point():
    main()


__starting_point()
