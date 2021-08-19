#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    a = sorted([A, B, C])
    o = sum([x & 1 for x in a])
    c = 0 < o and o < 3
    if o == 2:
        for i in range(3):
            a[i] += a[i] & 1
    elif o == 1:
        for i in range(3):
            a[i] += 1 - (a[i] & 1)
    print(((2 * a[2] - a[1] - a[0]) // 2 + c))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


def __starting_point():
    main()


__starting_point()
