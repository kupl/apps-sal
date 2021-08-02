from decimal import Decimal
from math import floor


def main():
    a, b = list(map(Decimal, input().split()))
    print((floor(a * b)))


def __starting_point():
    main()


__starting_point()
