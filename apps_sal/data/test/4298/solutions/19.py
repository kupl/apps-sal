def answer(n: int, d: int) -> int:
    from math import ceil
    return ceil(n / (d * 2 + 1))


def main():
    n, d = map(int, input().split())
    print(answer(n, d))


def __starting_point():
    main()


__starting_point()
