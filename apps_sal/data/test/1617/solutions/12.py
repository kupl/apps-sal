from math import sqrt, ceil
from collections import defaultdict
lim = int((10 ** 9) ** 0.5 + 100)


def sieve(N):
    """Dumb sieve of Eratosthemes, O(N*log(log(N)))"""
    b = [True] * (N + 1)
    b[0] = False
    b[1] = False
    lim = ceil(sqrt(N))
    i = 2
    while i <= lim:
        if b[i]:
            for n in range(i ** 2, N + 1, i):
                b[n] = False
        i += 1
    return [i for (i, b) in enumerate(b) if b]


P = sieve(lim)


def factor(n):
    """Given prime list, factorize n. Format as dict of factors with counts."""
    if n in P:
        return {n: 1}
    F = []
    for p in P:
        while n % p == 0:
            n //= p
            F.append(p)
        if n in P:
            F.append(n)
            break
    else:
        if n != 1:
            F.append(n)
    C = {}
    for f in F:
        if f not in C:
            C[f] = 0
        C[f] += 1
    return C


def divisors(n):
    """Generate divisors."""
    return divisors_from_factors(factor(n))


def divisors_from_factors(F):
    """Given factors, generate divisors."""
    D = {1}
    for f in F:
        D |= {f ** p * d for d in D for p in range(1, F[f] + 1)}
    return D


n = int(input())
D = divisors(n)
print(*sorted(((1 + n - d + 1) * n // d // 2 for d in D)))
