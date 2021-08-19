#!/usr/bin/env python3

from fractions import gcd
from operator import mul
from functools import reduce
from itertools import combinations


def eval_function(x): return lambda f: f(x)


@eval_function(int((10**9)**0.5))
def prime(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    index = 2
    for i in range(int(len(sieve)**0.5)):
        if sieve[i]:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = False
        index += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def factorized(n):
    factors = []
    for i in prime:
        if i**2 > n:
            break
        while not n % i:
            factors += [i]
            n //= i
    if n > 1:
        factors += [n]
    return factors


def solve(x, y, mod=None):
    if gcd(x, y) != x:
        return 0
    y = y // x
    c = pow(2, y - 1, mod)
    unique_factors = set(factorized(y))
    for i in range(1, len(unique_factors) + 1):
        for divisor in combinations(unique_factors, i):
            d = reduce(mul, divisor)
            c += (-1)**i * pow(2, y // d - 1, mod)
            c %= mod
    return c


def main():
    x, y = [int(n) for n in input().split()]
    print(solve(x, y, 10**9 + 7))


def __starting_point():
    main()


__starting_point()
