#!/usr/bin/env python3

def main():
    a, b, c, d = input()
    print(("Yes" if a == b == c or b == c == d else "No"))


def __starting_point():
    main()

__starting_point()
