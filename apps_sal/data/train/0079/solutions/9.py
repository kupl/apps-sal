# prime power always 0
# two prime powers?
#
# == 1 prime factor
#   trivial
# == 2 prime factors
#   p^a q^b
#   if a + b > 2: then fine
#   p*q
#   (remaining with p)
#   p*p*q
#   (remaining with q)
# >= 3 prime factors is fine
#   what ordering?
#   p*q*r
#   (all left with p)
#   p*q
#   (all left with q)
#   q*r
#   (all left with r)

from collections import defaultdict as dd, deque


def factor(n):
    factors = dd(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n != 1:
        factors[n] += 1
    return factors


def divisors(n):
    i = 1
    factors = []
    while i * i <= n:
        if n % i == 0:
            # If divisors are equal, print only one
            if n // i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n // i)
        i += 1
    return factors


t = int(input())

for _ in range(t):
    n = int(input())
    F = factor(n)
    D = set(divisors(n))
    D.remove(1)
    if len(F) == 1:
        print(*list(D))
        print(0)
        continue
    if len(F) == 2:
        p, q = list(F)
        exp = sum(F.values())
        if exp > 2:
            res = []
            D.remove(p * q)
            D.remove(p * p * q)

            divP = {d for d in D if d % p == 0}
            divQ = D - divP
            print(p * q, *divP, p * p * q, *divQ)
            print(0)
        else:
            print(p, p * q, q)
            print(1)
        continue
    first = 1
    for prime in F:
        first *= prime
    D.remove(first)
    Flist = list(F)
    res = [first]
    for i in range(len(Flist) - 1):
        p, q = Flist[i - 1], Flist[i]
        D.remove(p * q)
    for i in range(len(Flist) - 1):
        p, q = Flist[i - 1], Flist[i]
        div = {d for d in D if d % p == 0}
        D -= div
        res.extend(div)
        res.append(p * q)
    res.extend(D)
    print(*res)
    print(0)
