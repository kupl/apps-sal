import math


def answer(n: int) -> int:
    return int(math.sqrt(n)) ** 2


def main():
    n = int(input())
    print(answer(n))


def __starting_point():
    main()
__starting_point()
