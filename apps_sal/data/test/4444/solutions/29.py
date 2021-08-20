import sys
from itertools import chain


def solve(S: str, T: str):
    answer = T + S
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    S = next(tokens)
    T = next(tokens)
    answer = solve(S, T)
    print(answer)


def __starting_point():
    main()


__starting_point()
