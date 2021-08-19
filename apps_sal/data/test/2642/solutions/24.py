from math import gcd
from collections import defaultdict


def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return +1
    return 0


def power(a, b, m):
    res = 1
    base = a
    while b:
        if b & 1:
            res = res * base % m
        base = base * base % m
        b = b >> 1
    return res


N = int(input())
M = 1000000007
cnt = defaultdict(int)
case00 = 0
for _ in range(N):
    (a, b) = list(map(int, input().split()))
    if a == 0 and b == 0:
        case00 += 1
        continue
    s = sign(a) * sign(b)
    (a, b) = (abs(a), abs(b))
    g = gcd(a, b)
    (a, b) = (a // g, b // g)
    cnt[s, a, b] += 1
ans = 1
vis = set()
for (s, a, b) in list(cnt.keys()):
    if (s, a, b) in vis:
        continue
    if (-s, b, a) in cnt:
        mul = 1
        mul += power(2, cnt[s, a, b], M) - 1
        mul += power(2, cnt[-s, b, a], M) - 1
        ans = ans * (mul % M) % M
        vis.add((-s, b, a))
    else:
        ans = ans * power(2, cnt[s, a, b], M) % M
ans = (ans - 1 + M) % M
ans = (ans + case00) % M
print(ans)
