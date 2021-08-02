from math import gcd
from numpy import sign
mod = 1000000007
N = int(input())

d = {}
counter = 0

f = 0
l = 0

for _ in range(N):
    a, b = list(map(int, input().split()))
    if a == b == 0:
        counter += 1
    elif a == 0:
        f += 1
    elif b == 0:
        l += 1
    else:
        g = gcd(a, b)
        a, b = a // g, b // g
        if b < 0:
            a, b = -a, -b
        if (a, b) not in d:
            d[(a, b)] = 1
        else:
            d[(a, b)] += 1

answer = 1

group = set()
for (p, q), v in d.items():
    invp, invq = -q, p
    if invq < 0:
        invp, invq = -invp, -invq
    if not (invp, invq) in group:
        group.add((p, q))

for (p, q) in group:
    invp, invq = -q, p
    if invq < 0:
        invp, invq = -invp, -invq
    if (invp, invq) not in d:
        answer *= (2 ** d[(p, q)])
    else:
        answer *= ((2 ** d[(p, q)]) + (2 ** d[(invp, invq)]) - 1)

answer *= 2**f + 2**l - 1

print((answer + counter - 1) % mod)
