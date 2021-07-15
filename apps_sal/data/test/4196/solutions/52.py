from math import gcd

n, *a = list(map(int, open(0).read().split()))

l = [0] * n
r = [0] * n
for i in range(n - 1):
    l[i + 1] = gcd(l[i], a[i])
for i in range(n - 1, 0, -1):
    r[i - 1] = gcd(r[i], a[i])
print((max(gcd(l[i], r[i]) for i in range(n))))

