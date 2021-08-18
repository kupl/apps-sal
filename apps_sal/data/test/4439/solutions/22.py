import sys
from itertools import chain


def solve(A: int, B: int):
    answer = 6 - A - B
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    A = int(next(tokens))
    B = int(next(tokens))
    answer = solve(A, B)
    print(answer)


def __starting_point():
    main()


__starting_point()
