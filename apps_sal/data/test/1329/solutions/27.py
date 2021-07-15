N = int(input())

from collections import Counter
def factorize(n):
    d = Counter()
    m = 2
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
        m += 1
    if n > 1:
        d[n] += 1
    return d

fac = Counter()
for n in range(1,N+1):
    fac += factorize(n)

ans = 0
v4 = v2 = 0
for v in fac.values():
    if v >= 4:
        v4 += 1
    elif v >= 2:
        v2 += 1
t = v4 * (v4-1)//2 * (v4-2+v2)
if t > 0:
    ans += t

v24 = v2 = 0
for v in fac.values():
    if v >= 24:
        v24 += 1
    elif v >= 2:
        v2 += 1
t = v24 * (v24-1+v2)
ans += t

v14 = v4 = 0
for v in fac.values():
    if v >= 14:
        v14 += 1
    elif v >= 4:
        v4 += 1
t = v14 * (v14-1+v4)
ans += t

v74 = 0
for v in fac.values():
    if v >= 74:
        v74 += 1
ans += v74

print(ans)
