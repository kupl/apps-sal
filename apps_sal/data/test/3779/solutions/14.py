import math


def binpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return binpow(a, n - 1) * a
    else:
        b = binpow(a, n // 2)
        return b * b


(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a[i])
s = set()
d = gcd % k
isk = gcd
while d not in s:
    s.add(d)
    gcd += isk
    d = gcd % k
print(len(s))
print(*sorted(s))
