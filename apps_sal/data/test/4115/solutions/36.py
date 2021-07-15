#!/usr/bin/env python3


def solve(S: str):
    return sum([a != b for a, b in zip(S, reversed(S))]) // 2


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)


def __starting_point():
    main()

__starting_point()
