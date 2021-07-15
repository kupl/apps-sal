#!/usr/bin/env python3

def main():
    k, x = list(map(int, input().split()))
    print(("Yes" if 500 * k >= x else "No"))


def __starting_point():
    main()

__starting_point()
