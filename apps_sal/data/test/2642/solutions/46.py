from math import gcd
from collections import defaultdict
MOD = 10 ** 9 + 7
n = int(input())
ans = 1
C = defaultdict(int)
z = 0
r = 0
for i in range(n):
    (a, b) = map(int, input().split())
    if a == 0 and b == 0:
        r += 1
    elif b == 0:
        z += 1
    elif a == 0:
        C[0] += 1
    else:
        g = gcd(abs(a), abs(b))
        a //= g
        b //= g
        if a < 0:
            (a, b) = (-a, -b)
        C[a, b] += 1
D = tuple(C.items())
used = {0}
for (c, v) in D:
    if c in used:
        continue
    (a, b) = c
    if b > 0:
        (d, e) = (b, -a)
    else:
        (d, e) = (-b, a)
    ans *= pow(2, v, MOD) + pow(2, C[d, e], MOD) - 1
    ans %= MOD
    used.add((d, e))
ans *= pow(2, C[0], MOD) + pow(2, z, MOD) - 1
ans += r
ans -= 1
ans %= MOD
print(ans)
