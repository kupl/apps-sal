from collections import Counter
from itertools import permutations
n = int(input())


def factorization(n):
    p = 2
    fcr = []
    while p * p <= n:
        while n % p == 0:
            fcr.append(p)
            n //= p
        p += 1
    if n > 1:
        fcr.append(n)
    return fcr


fcr_l = []
for i in range(1, n + 1):
    fcr = factorization(i)
    fcr_l += fcr
c = Counter(fcr_l)
fcr_st = set(fcr_l)
ans = []
for (p, q, r) in permutations(fcr_st, 3):
    if c[p] >= 74:
        ans.append(p ** 74)
    if c[p] >= 24 and c[q] >= 2:
        ans.append(p ** 24 * q ** 2)
    if c[p] >= 14 and c[q] >= 4:
        ans.append(p ** 14 * q ** 4)
    if c[p] >= 4 and c[q] >= 4 and (c[r] >= 2):
        ans.append(p ** 4 * q ** 4 * r ** 2)
print(len(set(ans)))
