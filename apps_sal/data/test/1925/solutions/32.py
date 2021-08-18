import sys
from itertools import chain


def solve(A: int, B: int, N: int):
    if N >= B:
        x2 = B - 1
    else:
        x2 = N

    return (A * x2) // B


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    A = int(next(tokens))
    B = int(next(tokens))
    N = int(next(tokens))
    answer = solve(A, B, N)
    print(answer)


def __starting_point():
    main()


__starting_point()
