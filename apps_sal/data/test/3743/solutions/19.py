from math import sqrt, gcd


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all((n % i for i in range(3, int(sqrt(n)) + 1)))


def calculate_colors(n):
    primes = gen_primes()
    sqr_n = int(sqrt(n)) + 1
    if n == 1:
        return 1
    for p in primes:
        if n % p == 0:
            while n % p == 0:
                g = gcd(p, n)
                n = int(n // g)
            if n > 1:
                return 1
            else:
                return p
        if p > sqr_n:
            return n


n = int(input())
print(calculate_colors(n))
