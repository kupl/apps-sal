from math import gcd
MOD = 10 ** 9 + 7
N = int(input())
d = dict()
zeros = 0
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    if not any((a, b)):
        zeros += 1
        continue
    g = gcd(a, b) * (a // abs(a)) if all((a, b)) else a if a else b
    p = a // g, b // g
    d[p] = d.get(p, 0) + 1
done = set()
total = 1
for (a, b), v in d.items():
    if (b, -a) in done or (-b, a) in done:
        continue
    done.add((a, b))
    w = d.get((b, -a), 0) + d.get((-b, a), 0)
    total = total * (pow(2, v, MOD) + pow(2, w, MOD) - 1) % MOD
print((total + zeros - 1) % MOD)
