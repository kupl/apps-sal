from math import gcd
N = int(input())
mod = 10 ** 9 + 7
d = dict()
zeros = 0
for _ in range(N):
    (a, b) = map(int, input().split())
    if not any((a, b)):
        zeros += 1
        continue
    if all((a, b)):
        g = gcd(a, b) * (a // abs(a))
    elif a:
        g = a
    else:
        g = b
    p = (a // g, b // g)
    d[p] = d.get(p, 0) + 1
ans = 1
done = set()
for ((a, b), val) in d.items():
    if (-b, a) in done or (b, -a) in done:
        continue
    done.add((a, b))
    w = d.get((-b, a), 0) + d.get((b, -a), 0)
    ans *= pow(2, val) + pow(2, w) - 1
    ans %= mod
print((ans + zeros - 1) % mod)
