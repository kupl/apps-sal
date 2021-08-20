from math import gcd
n = int(input())
mod = 10 ** 9 + 7
count = {}
num = 0
for _ in range(n):
    (a, b) = map(int, input().split())
    if a == 0 and b == 0:
        num += 1
        continue
    if a * b != 0:
        g = gcd(a, b) * (b // abs(b))
    elif a != 0:
        g = a
    else:
        g = b
    l = (a // g, b // g)
    count[l] = count.get(l, 0) + 1
mem = set()
ans = 1
for ((x, y), z) in count.items():
    if x * y == 0:
        k = (y, x)
    else:
        k = (-1 * x // abs(x) * y, abs(x))
    if k in mem:
        continue
    mem.add((x, y))
    ans *= pow(2, z) + pow(2, count.get(k, 0)) - 1
    ans %= mod
print((ans + num - 1) % mod)
