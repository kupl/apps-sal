from typing import Set


def answer(n: int, s: Set[str]) -> int:
    return len(s)


def main():
    n = int(input())
    s = set(input() for _ in range(n))
    print((answer(n, s)))


def __starting_point():
    main()


__starting_point()
