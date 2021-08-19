from collections import defaultdict
from math import gcd

mod = 10 ** 9 + 7

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)
zero = 0
for a, b in ab:
    # zero　別処理
    if a == b == 0:
        zero += 1
        continue
    if a == 0:
        d[(0, 1)] += 1
        continue
    if b == 0:
        d[(1, 0)] += 1
        continue

    # a[i]が絶対に非負になるように
    if a < 0:
        a *= -1
        b *= -1
    g = gcd(a, b)
    d[(a // g, b // g)] += 1

all = n - zero
ans = 1
for k1, v in list(d.items()):
    k2 = (k1[1], -k1[0])
    if k2 in list(d.keys()):
        all -= v
        all -= d[k2]
        ans = ans * (pow(2, v, mod) + pow(2, d[k2], mod) - 1) % mod
ans = ans * pow(2, all, mod) % mod
print(((ans - 1 + zero) % mod))
