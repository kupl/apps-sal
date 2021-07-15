#!/usr/bin/env python3
import sys


def solve(X: int, Y: int):
    print(("Brown" if -1 <= X - Y <= 1 else "Alice"))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)


def __starting_point():
    main()

__starting_point()
