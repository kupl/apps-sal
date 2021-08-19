import sys
from itertools import chain
import numpy as np
import math


def factorize(n: int):
    """nを素因数分解する"""
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    if count > 0:
        arr = [(2, count)]
    else:
        arr = []
    for facter in range(3, n + 1, 2):
        if facter * facter > n:
            if n > 1:
                arr.append((n, 1))
            break
        count = 0
        while n % facter == 0:
            count += 1
            n = n // facter
        if count > 0:
            arr.append((facter, count))
    return arr


def case(n):
    t = 0
    i = 1
    while True:
        t += i
        if t > n:
            return i - 1
        i += 1


def solve(N: int):
    factors = factorize(N)
    answer = 0
    for (f, count) in factors:
        answer += case(count)
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    answer = solve(N)
    print(answer)


def __starting_point():
    main()


__starting_point()
