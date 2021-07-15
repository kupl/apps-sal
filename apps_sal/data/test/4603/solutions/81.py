#!/usr/bin/env python3

def main():
    a, b, c, d = (int(input()) for i in range(4))
    print((min(a, b) + min(c, d)))


def __starting_point():
    main()

__starting_point()
