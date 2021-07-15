import sys
from math import sqrt, gcd
from itertools import product
from functools import reduce
from operator import mul


def get_primes(n: int):
    from itertools import chain
    from array import array
    primes = [2, 3]
    is_prime = (array('b', (0, 0, 1, 1, 0, 1, 0)) +
                array('b', (1, 0, 0, 0, 1, 0))*((n-1)//6))

    for i in chain.from_iterable((list(range(5, n+1, 6)), list(range(7, n+1, 6)))):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*3, n+1, i*2):
                is_prime[j] = 0

    return primes


x, y = list(map(int, input().split()))
primes = get_primes(int(sqrt(x))+1)
_x = x

pfac, pfac_cnt = [], []
for p in primes:
    if _x % p == 0:
        pfac.append(p)
        pfac_cnt.append(0)
        while _x % p == 0:
            pfac_cnt[-1] += 1
            _x //= p
if _x > 1:
    pfac.append(_x)
    pfac_cnt.append(1)

if not pfac:
    print(y)
    return


def solve(y, g):
    z = 0
    for ea in product(*(list(range(e+1)) for e in pfac_cnt)):
        divisor = reduce(mul, (p**e for p, e in zip(pfac, ea)))
        if divisor % g == 0 and divisor > g:
            z = max(z, divisor * (y // divisor))

    return z


ans = 0

while y:
    g = gcd(x, y)
    z = solve(y, g)
    ans += (y - z) // g
    y = z

print(ans)

