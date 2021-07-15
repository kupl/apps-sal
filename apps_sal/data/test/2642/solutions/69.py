from math import gcd
from collections import defaultdict
mod = 10**9+7
_, *S = open(0)
mp = defaultdict(lambda: [0, 0])
O = 0
for s in S:
    a, b = list(map(int, s.split()))
    if a == b == 0:
        O += 1
    else:
        g = gcd(a, b)
        a //= g
        b //= g
        if a < 0 or a == 0 < b:
            a, b = -a, -b
        f = 0
        if b < 0:
            a, b, f = -b, a, 1
        mp[(a, b)][f] += 1
ans = 1
for k in mp:
    x, y = mp[k]
    ans = ans*(pow(2, x, mod)+pow(2, y, mod)-1) % mod
print(((ans+O-1) % mod))

