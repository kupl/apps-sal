from collections import Counter
from itertools import chain


def prime_set(N):
    """
    Nまでの素数のsetを返す
    """
    if N < 4:
        return ({}, {}, {2}, {2, 3})[N]
    Nsq = int(N ** 0.5 + 0.5) + 1
    primes = {2, 3} | set(chain(range(5, N + 1, 6), range(7, N + 1, 6)))
    for i in range(5, Nsq, 2):
        if i in primes:
            primes -= set(range(i * i, N + 1, i * 2))
    return primes


def prime_factorization(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res.append((i, cnt))
    if n > 1:
        res.append((n, 1))
    return res


N = int(input())
primes = {p: 0 for p in prime_set(100)}
for i in range(2, N + 1):
    pf = prime_factorization(i)
    for p, f in pf:
        primes[p] += f


n2 = n4 = n14 = n24 = n74 = 0
for v in primes.values():
    if v >= 74:
        n74 += 1
    if v >= 24:
        n24 += 1
    if v >= 14:
        n14 += 1
    if v >= 4:
        n4 += 1
    if v >= 2:
        n2 += 1

ans = 0
if n74:
    ans += n74
if n24:
    ans += n24 * (n2 - 1)
if n14:
    ans += n14 * (n4 - 1)
if n4 >= 2 and n2:
    ans += n4 * (n4 - 1) // 2 * (n2 - 2)

print(ans)
