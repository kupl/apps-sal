from math import gcd

n, k = map(int, input().split())
a, b = map(int, input().split())


def stop(x, y):
    d = (y - x + n * k * 2) % (n * k)
    g = gcd(n * k, d)
    return n * k // g


mn, mx = 10**20, 0
s = [-a, a]
for x in s:
    for i in range(n):
        f = [i * k - b, i * k + b]
        for y in f:
            cur = stop(x, y)
            mn = min(mn, cur)
            mx = max(mx, cur)

print(mn, mx)
