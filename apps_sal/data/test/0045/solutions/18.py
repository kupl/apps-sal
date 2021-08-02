from math import sqrt
n, k = list(map(int, input().split()))


def f(s):
    for v in range(1, 1 + int(sqrt(n))):
        if n % v == 0:
            yield v
            yield n // v


s = k * (k + 1) // 2
v = set(x for x in f(s) if x <= n // s)
if v:
    gcd = max(v)
    print(*list(range(gcd, gcd * k, gcd)), n - gcd * (k - 1) * k // 2)
else:
    print(-1)
