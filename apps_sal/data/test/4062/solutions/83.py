from itertools import product


def answer(a: int, b: int, c: int, d: int) -> int:
    return max(x * y for x, y in product((a, b), (c, d)))


def main():
    a, b, c, d = map(int, input().split())
    print(answer(a, b, c, d))


def __starting_point():
    main()


__starting_point()
