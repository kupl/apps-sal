#!/usr/bin/env python3
from functools import reduce
from operator import mul


def get_value(function):
    return function()


@get_value
def primes(size=10**6):
    sieve = [True for _ in (list(range(size)))]
    sieve[0] = False
    sieve[1] = False
    prime = 2
    while prime < size:
        for compound in range(2*prime, size, prime):
            sieve[compound] = False
        try:
            prime = sieve.index(True, prime + 1)
        except ValueError:
            break
    return [number for number, is_prime in enumerate(sieve) if is_prime]


def factorized(number):
    if number == 1:
        return [1]
    factors = []
    for prime in primes:
        if prime**2 > number:
            break
        while number % prime == 0:
            factors += [prime]
            number //= prime
    if number > 1:
        factors += [number]
    return factors


def main():
    print(reduce(mul, set(factorized(int(input())))))


def __starting_point():
    main()

__starting_point()
