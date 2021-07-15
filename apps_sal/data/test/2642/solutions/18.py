from math import gcd
from collections import Counter

mod = 10 ** 9 + 7

N, *AB = map(int, open(0).read().split())

def std(a, b):
    if a == 0:
        return (0, 1)

    g = gcd(a, b)
    a, b = a // g, b // g
    return (a, b) if a > 0 else (-a, -b)

C = Counter()
orig = 0
for a, b in zip(*[iter(AB)] * 2):
    if a == b == 0:
        orig += 1
    else:
        C[std(a, b)] += 1

ans = 1
cnt = 0
for (a, b), v in C.items():
    if b > 0:
        if (b, -a) in C:
            ans *= -1 + pow(2, v, mod) + pow(2, C[(b, -a)], mod)
            ans %= mod
        else:
            cnt += v
    elif (-b, a) not in C:
        cnt += v

ans *= pow(2, cnt, mod)
ans += orig - 1

print(ans % mod)
