from collections import Counter
from functools import reduce


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


def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x
        x = x * x
        n //= 2
    return K * x


def xgcd(a, b):
    (x0, y0, x1, y1) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a // b, b, a % b)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (a, x0, y0)


def modinv(a, m):
    (g, x, y) = xgcd(a, m)
    return x % m


def modmul(a, b):
    return a * b % 1000000007


def comb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(modmul, range(n, n - r, -1))
    under = reduce(modmul, range(1, r + 1))
    return over * modinv(under, 1000000007)


(N, M) = (int(x) for x in input().split())
ans = 1
if M == 1:
    print('1')
else:
    a = Counter(prime_factorize(M))
    for x in a.values():
        ans = ans * comb(N + x - 1, x) % 1000000007
    print(ans)
