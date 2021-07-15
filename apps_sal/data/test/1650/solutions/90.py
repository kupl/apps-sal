#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

MOD = 1000000007  # type: int


def solve(L: str):
    a = 1
    b = 1
    for Li in L:
        if Li == "1":
            a *= 3
            a %= MOD
            b *= 2
            b %= MOD
        else:
            a += (a - b) * 2
            a %= MOD
    print(a)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = next(tokens)  # type: str
    solve(L)


def __starting_point():
    main()

__starting_point()
