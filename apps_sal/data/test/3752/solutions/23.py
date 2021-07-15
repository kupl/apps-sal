R = lambda: map(int, input().split())
k, d, t = R()
p = (k // d + (1 if k % d else 0)) * d
l, r = 0, 2 * 10**18
while (r - l) / max(1, r) > 10**-10:
    m = (l + r) / 2
    ht = m // p * k + min(k, m % p)
    lt = m // p * (p - k) + max(0, m % p - k)
    if ht / t + lt / (t * 2) < 1:
        l = m
    else:
        r = m
print(l)
