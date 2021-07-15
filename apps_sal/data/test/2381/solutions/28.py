from math import log
mod = int(1e9) + 7
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()

def sign(v):
    if v == 0:
        return 0
    return 1 if v > 0 else -1

pref = [(0, 1)] * (n + 1)
suf = [(0, 1)] * (n + 1)

c = 1
sm = 0
sgn = 1
for j in range(n):
    c = c * a[j] % mod
    sgn *= sign(a[j])
    if a[j] != 0:
        sm += log(abs(a[j]))
    pref[j + 1] = (sgn * sm, c, sgn)

c = 1
sm = 0
sgn = 1
for j in range(n):
    c = c * a[n - j - 1] % mod
    sgn *= sign(a[n - j - 1])
    if a[n - j - 1] != 0:
        sm += log(abs(a[n - j - 1]))
    suf[j + 1] = (sgn * sm, c, sgn)

m = max(pref[k], suf[k])
for i in range(1, k):
    sgn = pref[i][2] * suf[k - i][2]
    pm = pref[i][1] * suf[k - i][1] % mod
    sm = abs(pref[i][0]) + abs(suf[k - i][0])
    m = max(m, (sgn * sm, pm, sgn))

    
print((m[1]))

