from collections import defaultdict
from math import gcd
N = int(input())
mod = 10**9 + 7
D = defaultdict(int)
corner = 0
D[(0, 1)] = 0
D[(1, 0)] = 0
for i in range(N):
    x, y = map(int, input().split())
    if x * y != 0:
        x, y = x // gcd(x, y), y // gcd(x, y)
        if y > 0:
            D[(x, y)] += 1
        elif y < 0:
            D[(-x, -y)] += 1
    else:
        if x == 0 and y == 0:
            corner += 1
            continue
        else:
            if x == 0:
                D[(0, 1)] += 1
            elif y == 0:
                D[(1, 0)] += 1
ans = corner
c = 1
sub = []
for x, y in D.keys():
    if x < 0 and y > 0:
        if not (y, -x) in D.keys():
            sub.append((y, -x))
for some in sub:
    D[some] = 0

K = list(D.keys())
for x, y in K:
    if x > 0 and y > 0:
        a = D[(x, y)]
        b = D[(-y, x)]
        c *= (pow(2, a, mod) + pow(2, b, mod) - 1)
        c %= mod
    elif y == 0:
        a = D[(1, 0)]
        b = D[(0, 1)]
        c *= (pow(2, a, mod) + pow(2, b, mod) - 1)
        c %= mod
ans += c - 1

print(ans % mod)
