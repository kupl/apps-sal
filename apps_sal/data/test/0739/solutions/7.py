L, a, b, m = map(int, input().split())
ans = 0
for k in range(1, 37):
    l = (10**(k - 1) - a + b - 1) // b
    r = (10**k - a + b - 1) // b
    l = max(l, 0)
    r = min(r, L)
    if l >= r:
        continue
    d = r - l
    c = a + b * (r - 1)
    t = 10**k - 1
    x = b * pow(10, k, m * t * t) * (pow(10, k * (d - 1), m * t * t) - 1)
    x %= m * t * t
    x //= t
    y = (c - (d - 1) * b) * pow(10, d * k, m * t)
    y %= m * t
    s = x + y - c
    s %= m * t
    s //= t
    ans *= pow(10, d * k, m)
    ans += s
    ans %= m
print(ans)
