import math


def reduce_fraction(n, m):
    k = math.gcd(n, m)
    if n > 0 and m < 0 or (n < 0 and m < 0):
        n = -n
        m = -m
    if n == 0 and m < 0:
        m *= -1
    return (n // k, m // k)


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
s = 0
for i in range(n):
    if a[i] != 0:
        x = reduce_fraction(b[i], a[i])
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    elif b[i] == 0:
        s += 1
maxs = 0
for i in d:
    maxs = max(maxs, d[i])
print(maxs + s)
