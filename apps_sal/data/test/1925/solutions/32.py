#!/usr/bin/env python3
import sys
from itertools import chain

# floor(A x / B) - A * floor(x / B)
#
# x = B * x1 + x2  : (x2 < B) とする
#
# = floor(A (B*x1+x2) / B) - A floor((B*x1+x2) / B)
# = A x1 + floor(A x2 / B) - A x1
# = floor(A x2 / B)


def solve(A: int, B: int, N: int):
    if N >= B:
        x2 = B - 1
    else:
        x2 = N

    return (A * x2) // B


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    answer = solve(A, B, N)
    print(answer)


def __starting_point():
    main()

__starting_point()
