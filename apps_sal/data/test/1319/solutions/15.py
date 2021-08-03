import operator
from collections import Counter

from functools import reduce


def solve(primes):
    products = 1
    for x in primes.values():
        products *= x + 1
        products %= 2 * (10 ** 9 + 6)

    n = 1
    for x, y in primes.items():
        n *= pow(x, y * (y + 1) // 2 * products // (y + 1), 10 ** 9 + 7)
        n %= (10 ** 9 + 7)

    return n


def main():
    m = int(input())
    primes = Counter(map(int, input().split()))
    print(solve(primes))


def __starting_point():
    main()


__starting_point()
