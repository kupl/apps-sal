n, h, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

t, p, i = 0, 0, 0
while i < len(a) or p > 0:
    while i < len(a) and p + a[i] <= h:
        p += a[i]
        i += 1
    if p >= k:
        q = p // k
        p = p - q * k
        t += q
    else:
        p = 0
        t += 1
print(t)
