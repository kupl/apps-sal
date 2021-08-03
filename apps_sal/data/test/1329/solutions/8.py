from collections import defaultdict
import math


def main():
    def factorization(num):
        nonlocal d
        if num in primes:
            d[num] += 1
            return
        for prime in primes:
            if num % prime == 0:
                count = 0
                while num % prime == 0:
                    count += 1
                    num //= prime
                d[prime] += count

    def generate_primes(num):
        if num == 1:
            return []
        primes = list(range(2, num + 1))
        i, p = 0, 1
        while p <= math.sqrt(num):
            if primes[i] != 0:
                p = primes[i]
                primes = [prime if (prime % p != 0 or prime == p) else 0 for prime in primes]
            i += 1
        return set(p for p in primes if p != 0)

    n = int(input())
    d = defaultdict(lambda: 1)
    primes = generate_primes(100)
    for i in range(1, n + 1):
        factorization(i)
    c = [0] * 6
    for v in list(d.values()):
        if v >= 3:
            c[0] += 1
        if v >= 75:
            c[5] -= 1
        elif v >= 25:
            c[4] -= 1
        elif v >= 15:
            c[3] -= 1
        elif v >= 5:
            c[2] -= 1
        elif v >= 3:
            c[1] -= 1
    s = 0
    for i in range(6):
        s += c[i]
        c[i] = s
    print((c[1] * (c[1] - 1) * (c[0] - 2) // 2 + c[3] * (c[0] - 1) + c[2] * (c[1] - 1) + c[4]))


def __starting_point():
    main()


__starting_point()
