# 1390. Four Divisors
# version 2, with optimized prime-finding.

import math


def remove(lst, index):
    assert lst
    tail = len(lst) - 1
    lst[index], lst[tail] = lst[tail], lst[index]
    lst.pop()


def swap_min(lst):
    if not lst:
        return
    argmin = min(range(len(lst)), key=lambda i: lst[i])
    lst[0], lst[argmin] = lst[argmin], lst[0]


def find_primes(top):
    candidates = list(range(2, top))
    primes = []
    while candidates:
        # here, candidates[0] is the least element.
        latest_prime = candidates[0]
        primes.append(latest_prime)
        remove(candidates, 0)
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] % latest_prime == 0:
                remove(candidates, i)

        swap_min(candidates)
        # before continuing, set candidates[0] to be the least element.
    return primes


def find_prime_factor(n, primes):
    for p in primes:
        if n % p == 0:
            return p


def div4(n, primes, setprimes):
    if n <= 3:
        return 0
    elif n in setprimes:
        return 0
    else:
        p1 = find_prime_factor(n, primes)
        if p1 is None:
            return 0
        p2 = find_prime_factor(n // p1, primes)
        if p2 is None:
            p2 = n // p1
        if p1 * p2 == n and p1 != p2:
            # success
            return (1 + p1) * (1 + p2)
        elif p1 ** 3 == n:
            # success
            return (1 + p1) * (1 + p1**2)
        else:
            return 0


def sum_four_divisors(arr):
    top = math.ceil(math.sqrt(max(arr) + 5))
    primes = find_primes(top)
    setprimes = set(primes)
    return sum(div4(elem, primes, setprimes) for elem in arr)


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum_four_divisors(nums)
