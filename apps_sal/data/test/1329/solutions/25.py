from collections import *


def factorize(n):
    fct = []
    for i in range(2, int(n ** 0.5) + 1):
        c = 0
        while n % i == 0:
            n //= i
            c += 1
        if c > 0:
            fct.append((i, c))
    if n > 1:
        fct.append((n, 1))
    return fct


N = int(input())
cnt = defaultdict(int)
for i in range(1, N + 1):
    fct = factorize(i)
    for (p, c) in fct:
        cnt[p] += c
(ov74, ov24, ov14, ov4, ov2) = (0, 0, 0, 0, 0)
for v in cnt.values():
    if v >= 74:
        ov74 += 1
    if v >= 24:
        ov24 += 1
    if v >= 14:
        ov14 += 1
    if v >= 4:
        ov4 += 1
    if v >= 2:
        ov2 += 1
ans = ov74 + ov24 * (ov2 - 1) + ov14 * (ov4 - 1) + ov4 * (ov4 - 1) // 2 * (ov2 - 2)
print(ans)
