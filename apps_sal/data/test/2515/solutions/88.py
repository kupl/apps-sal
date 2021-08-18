import numpy as np
import math


def primes(x):
    if x < 2:
        return []

    primes = [i for i in range(x)]
    primes[1] = 0

    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


pr = primes(100000)
d = [0] * 100001
ans = [0] * 100001

for j in pr:
    d[j] = 1

for k in pr:
    tmp = (k + 1) // 2
    if d[tmp] == 1:
        ans[k] = 1

cum = np.cumsum(ans)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    i1 = cum[l - 1]
    i2 = cum[r]
    print(i2 - i1)
