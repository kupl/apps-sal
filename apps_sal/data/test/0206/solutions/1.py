from math import gcd
(m, a, b) = list(map(int, input().split()))
g = gcd(a, b)
vis = [0] * (a + b + 1)
vis[0] = 1
nvis = 1
count = 0
last = 0
t = 0
while True:
    if t >= b:
        t -= b
        if vis[t]:
            break
        vis[t] = 1
        nvis += 1
    else:
        t += a
        if t > m:
            break
        if t > last:
            count += (t - last) * nvis
            last = t
        if vis[t]:
            break
        vis[t] = 1
        nvis += 1
if t > m:
    count += (m - last + 1) * nvis
else:

    def sumto(n):
        whole = n // g + 1
        r = whole * (whole + 1) // 2 * g
        corr = whole * (g - 1 - n % g)
        r -= corr
        return r
    count += sumto(m) - sumto(last - 1)
print(count)
