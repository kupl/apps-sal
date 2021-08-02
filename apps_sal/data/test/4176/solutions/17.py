#!/usr/bin/env python3
import sys
from itertools import chain


def gcd(a, b):
    """最大公約数
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """最小公倍数
    """
    return a * b // gcd(a, b)


def solve(A: int, B: int):
    answer = lcm(A, B)
    return answer


def main():
    A, B = list(map(int, input().split()))
    answer = solve(A, B)
    print(answer)


def __starting_point():
    main()


__starting_point()
