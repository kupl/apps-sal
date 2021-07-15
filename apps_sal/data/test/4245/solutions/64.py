from math import ceil


def answer(a: int, b: int) -> int:
    return ceil((b - 1) / (a - 1))


def main():
    a, b = list(map(int, input().split()))
    print((answer(a, b)))


def __starting_point():
    main()

__starting_point()
