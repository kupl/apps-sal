from math import gcd
mod = 1000000007
n = int(input())
ab00 = 0
abx0 = 0
ab0x = 0
p = []
m = []
for _ in range(n):
    (i, j) = map(int, input().split())
    if i == 0:
        if j == 0:
            ab00 += 1
        else:
            ab0x += 1
        continue
    elif j == 0:
        abx0 += 1
        continue
    k = gcd(i, j)
    i //= k
    j //= k
    if i > 0:
        if j > 0:
            p.append((i, j))
        else:
            m.append((-j, i))
    elif j > 0:
        m.append((j, -i))
    else:
        p.append((-i, -j))
m.sort()
p.sort()
ans = pow(2, ab0x, mod) + pow(2, abx0, mod) - 1
ans %= mod
mi = 0
pi = 0
while mi < len(m) and pi < len(p):
    if m[mi] == p[pi]:
        mi += 1
        mnum = 1
        while mi < len(m) and m[mi] == m[mi - 1]:
            mi += 1
            mnum += 1
        pi += 1
        pnum = 1
        while pi < len(p) and p[pi] == p[pi - 1]:
            pi += 1
            pnum += 1
        ans *= pow(2, mnum, mod) + pow(2, pnum, mod) - 1
        ans %= mod
    elif m[mi] < p[pi]:
        mi += 1
        mnum = 1
        while mi < len(m) and m[mi] < p[pi]:
            mi += 1
            mnum += 1
        ans *= pow(2, mnum, mod)
        ans %= mod
    else:
        pi += 1
        pnum = 1
        while pi < len(p) and p[pi] < m[mi]:
            pi += 1
            pnum += 1
        ans *= pow(2, pnum, mod)
        ans %= mod
ans *= pow(2, len(p) - pi, mod)
ans %= mod
ans *= pow(2, len(m) - mi, mod)
ans %= mod
ans = (ans - 1 + ab00) % mod
print(ans)
