from collections import defaultdict
from math import gcd
MOD = 10 ** 9 + 7
n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)


def kikaku(a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    if a < 0:
        return (-a, -b)
    return (a, b)


Dpos = defaultdict(int)
Dneg = defaultdict(int)
zerozero = 0
azero = 0
bzero = 0
for l in L:
    a = l[0]
    b = l[1]
    if a == b == 0:
        zerozero += 1
        continue
    if a == 0:
        azero += 1
        continue
    if b == 0:
        bzero += 1
        continue
    (a, b) = kikaku(a, b)
    if b > 0:
        Dpos[a, b] += 1
    else:
        Dneg[a, -b] += 1
        Dpos[-b, a] += 0
r = 1
for (k, v) in list(Dpos.items()):
    (a, b) = k
    j = Dneg[b, a]
    r *= pow(2, v, MOD) + pow(2, j, MOD) - 1
    r %= MOD
r *= pow(2, azero, MOD) + pow(2, bzero, MOD) - 1
r %= MOD
r -= 1
r %= MOD
ans = r + zerozero
ans %= MOD
print(ans)
