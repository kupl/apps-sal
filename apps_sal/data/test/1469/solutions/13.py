#!/usr/bin/env python3
import sys


def solve(L: int):
    sL = "{:b}".format(L)
    N = len(sL)
    M = 2 * (N - 1) + sL.count("1") - 1
    print((N, M))
    for i in range(N - 1):
        print((i + 1, i + 2, 0))
        print((i + 1, i + 2, 2 ** i))
    for i, c in enumerate(reversed(sL[1:])):
        if c == "0":
            continue
        print((i + 1, N, int(sL[:-i - 1], 2) * 2 ** (i + 1)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    solve(L)


def __starting_point():
    main()

__starting_point()
