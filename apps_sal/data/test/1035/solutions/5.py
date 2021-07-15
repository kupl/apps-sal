from math import gcd
from typing import List, Tuple


def pf(n: int) -> List[Tuple[int,int]]:
    r = []
    for p in range(2, n):
        if p * p > n:
            break
        e = 0
        if n % p == 0:
            while(n % p == 0):
                n //= p
                e += 1
            r.append((p, e))
    if n != 1:
        r.append((n, 1))
    return r

a,b = map(int, input().split())
apf = pf(a)
bpf = pf(b)
aps = {p for p,e in apf}
bps = {p for p,e in bpf}
print(len(aps&bps)+1)
