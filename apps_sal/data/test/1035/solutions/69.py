from math import gcd
from typing import List, Tuple


def pf(n: int) -> List[Tuple[int, int]]:
    r = []
    for p in range(2, n):
        if p * p > n:
            break
        e = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                e += 1
            r.append((p, e))
    if n != 1:
        r.append((n, 1))
    return r


(a, b) = list(map(int, input().split()))
r = pf(gcd(a, b))
print(len(r) + 1)
