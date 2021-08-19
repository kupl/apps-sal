import itertools as it
from collections import defaultdict
import os
import sys


def sieve(n):
    is_prime = [True] * n

    for candidate in it.chain([2], list(range(3, int(n ** 0.5) + 1, 2))):
        if is_prime[candidate]:
            for k in range(2 * candidate, n, candidate):
                is_prime[k] = False

    primes = [idx for idx, k in enumerate(is_prime) if idx >= 2 and k]
    return primes


def factorize(n, primes, k):
    factors = []
    number = n
    for f in primes:
        count = 0
        while number % f == 0:
            count += 1
            number //= f

        if count % k:
            factors.append((f, count % k))

        if f > number:
            break

    if number > 1:
        factors.append((number, 1))

    return tuple(factors)


def solve(arr, k):
    total = 0
    d = defaultdict(int, {})
    primes = sieve(int(1e5 ** 0.5) + 10)
    for a in arr:
        fac = factorize(a, primes, k)
        fac_complement = tuple((f, k - count) for f, count in fac)
        total += d[fac_complement]
        d[fac] += 1

    return total


def pp(input):
    # T = int(input())
    # for t in range(T):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    print(solve(arr, k))


if "paalto" in os.getcwd():
    from string_source import string_source, codeforces_parse

    pp(
        string_source(
            """6 3
1 3 9 8 24 1"""
        )
    )
else:
    pp(sys.stdin.readline)
