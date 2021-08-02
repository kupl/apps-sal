from math import gcd
from collections import defaultdict

N = int(input())
d = {}
MOD = 10**9 + 7
zall = 0

for _ in range(N):
    A, B = list(map(int, input().split()))

    if A == 0 and B == 0:
        zall += 1
    else:
        if A and B:
            if A < 0 and B < 0:
                A *= -1
                B *= -1
            elif A < 0 and B > 0:
                A *= -1
                B *= -1

            g = gcd(A, B)
            A //= g
            B //= g
        elif A == 0:
            B = 1
        elif B == 0:
            A = 1

        if (A, B) in d:
            d[(A, B)] += 1
        else:
            d[(A, B)] = 1

ans = 1
used = defaultdict(int)

for (i, j), v in list(d.items()):
    if used[(i, j)]: continue
    used[(i, j)] = 1
    buf = 0

    if j > 0:
        if (j, -i) in d:
            used[(j, -i)] = 1
            buf = d[(j, -i)]
        else:
            buf = 0
    else:
        if (-j, i) in d:
            used[(-j, i)] = 1
            buf = d[(-j, i)]
        else:
            buf = 0

    ans *= (pow(2, buf, MOD) + pow(2, v, MOD) - 1)
    ans %= MOD

print(((ans + zall - 1) % MOD))
