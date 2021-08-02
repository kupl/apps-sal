import sys
a, b, w, x, c = map(int, input().split())
if c <= a:
    print(0)
    return
d = c - a
ans = 0
if b // x >= d:
    print(d)
    return
ans += (b // x + 1)
d -= (b // x)
b = w - (x - b % x)
b0 = b
g = 0
det = 0
while (1):
    if b // x >= d:
        print(ans + d)
        return
    g += (b // x + 1)
    det += (b // x)
    ans += (b // x + 1)
    d -= (b // x)
    b = w - (x - b % x)
    if b == b0:
        break

if d > det:
    k = d // det
    if (d % det == 0):
        k -= 1
    d -= det * k
    ans += k * g
while (1):
    if b // x >= d:
        print(ans + d)
        return
    ans += (b // x + 1)
    d -= (b // x)
    b = w - (x - b % x)
