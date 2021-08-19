import sys
from math import sqrt, floor
from collections import Counter


def factorize(n):
    limit = floor(sqrt(n))
    factor = Counter()
    p = 2
    while n % p == 0:
        factor[p] += 1
        n //= p
    for p in range(3, limit + 1, 2):
        while n % p == 0:
            factor[p] += 1
            n //= p
    if n > 1:
        factor[n] += 1
    return factor


def make_divisors(n):
    result = [1]
    for (p, e) in factorize(n).items():
        result = [x * p ** i for i in range(e + 1) for x in result]
    return sorted(result)


(n, k) = map(int, input().split())
divisors = make_divisors(n)
if k > len(divisors):
    ans = -1
else:
    ans = divisors[k - 1]
print(ans)
