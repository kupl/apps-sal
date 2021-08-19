#!/usr/bin/env python3

def main():
    a, b = list(map(int, input().split()))
    print((a + b if a + b < 10 else 'error'))


def __starting_point():
    main()


__starting_point()
