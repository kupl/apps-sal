import math
import collections

def prime_factorize(n):
    s = []
    while n % 2 == 0:
        s.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            s.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        s.append(n)
    return s

a, b = map(int, input().split())

g = math.gcd(a, b)
c = collections.Counter(prime_factorize(g))

print(len(c.values()) + 1)
