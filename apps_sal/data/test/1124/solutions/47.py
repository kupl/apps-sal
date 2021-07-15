from functools import reduce
from math import gcd
from typing import List


def solve(n: int, a: List[int]) -> int:
    return reduce(gcd, a)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print((solve(n, a)))


def __starting_point():
    main()

__starting_point()
