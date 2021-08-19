import math


def answer(n: int) -> int:
    return math.factorial(n) % (10 ** 9 + 7)


def main():
    n = int(input())
    print(answer(n))


def __starting_point():
    main()


__starting_point()
