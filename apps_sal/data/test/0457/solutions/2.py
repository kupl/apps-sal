from math import sqrt, ceil


def primes(x):
    ox = x
    l = []
    cp = 3
    if x % 2 == 0:
        l.append(2)
    while x % 2 == 0:
        x //= 2
    while cp <= ceil(sqrt(ox)):
        if x % cp == 0:
            l.append(cp)
        while x % cp == 0:
            x //= cp
        cp += 2
    if x != 1:
        l.append(x)
    return l


mo = 10 ** 9 + 7
(x, n) = list(map(int, input().split()))
pi = primes(x)
s = 1
for p in pi:
    pk = p
    while pk <= n:
        s *= pow(p, n // pk, mo)
        s %= mo
        pk *= p
print(s)
