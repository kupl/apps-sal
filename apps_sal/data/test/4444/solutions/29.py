#!/usr/bin/env python3
import sys
from itertools import chain


def solve(S: str, T: str):
    answer = T + S
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    answer = solve(S, T)
    print(answer)


def __starting_point():
    main()


__starting_point()
