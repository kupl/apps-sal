from fractions import Fraction
from typing import List


def answer(n: int, a: List[int]) -> float:
    f = Fraction(1, sum((Fraction(1, i) for i in a)))
    return f.numerator / f.denominator


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n, a))


def __starting_point():
    main()


__starting_point()
