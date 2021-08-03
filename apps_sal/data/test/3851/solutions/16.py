from math import gcd

n, k = map(int, input().split())
a, b = map(int, input().split())


def stop(x, y):
    d = (y - x + n * k * 2) % (n * k)
    g = gcd(n * k, d)
    return n * k // g


mn, mx = 10**20, 0
for x in [-a, a]:
    for i in range(n):
        for y in [i * k - b, i * k + b]:
            cur = stop(x, y)
            mn = min(mn, cur)
            mx = max(mx, cur)

print(mn, mx)
