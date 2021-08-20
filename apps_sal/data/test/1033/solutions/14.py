(n, h) = input().split(' ')
n = int(n)
h = int(h)
l = 1
r = 1000000000000000000
while l < r:
    k = (l + r) // 2
    u = 0
    if k <= h:
        u = k * (k + 1) // 2
    else:
        u = h * (h + 1) // 2
        u += h * (k - h)
        d = k - h
        if d % 2 == 0:
            u += d * d // 4
        else:
            d //= 2
            u += d * (d + 1)
    if u < n:
        l = k + 1
    else:
        r = k
print(l)
