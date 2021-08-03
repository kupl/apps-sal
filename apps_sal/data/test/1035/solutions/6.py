import collections
import math
A, B = map(int, input().split())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


c = prime_factorize(math.gcd(A, B))
c = collections.Counter(c)
c = c.values()

print(len(c) + 1)
