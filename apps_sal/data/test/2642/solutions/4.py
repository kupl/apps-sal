from math import gcd
n = int(input())
mod = 1000000007
z = 0
d = {}
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if not any((a, b)):
        z += 1
        continue
    if a == 0:
        d[0, 1] = d.get((0, 1), 0) + 1
        continue
    if b == 0:
        d[1, 0] = d.get((1, 0), 0) + 1
        continue
    g = gcd(a, b)
    s = a // abs(a)
    (a, b) = (a // g * s, b // g * s)
    d[a, b] = d.get((a, b), 0) + 1
done = set()
ans = 1
for ((a, b), v) in list(d.items()):
    if (a, b) in done:
        continue
    done.add((a, b))
    done.add((-b, a))
    done.add((b, -a))
    w = d.get((-b, a), 0) + d.get((b, -a), 0)
    ans *= pow(2, v, mod) + pow(2, w, mod) - 1
    ans %= mod
ans = (ans + z - 1 + mod) % mod
print(ans)
