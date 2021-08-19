from math import sqrt, gcd


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
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
    return all(n % i for i in range(3, int(sqrt(n)) + 1))


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
