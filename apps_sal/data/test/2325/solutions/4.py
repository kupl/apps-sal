from math import sqrt
from itertools import chain
import sys
input = sys.stdin.readline

mod = 10**9 + 7

ub = 1010
ub_sqrt = int(sqrt(ub)) + 1
primes = {2, 3} | set(chain(range(5, ub, 6), range(7, ub, 6)))
du = primes.difference_update
for n in chain(range(5, ub_sqrt, 6), range(7, ub_sqrt, 6)):
    if n in primes:
        du(range(n * 3, ub, n * 2))

m = 10**6 + 100
fac, inv = [1] * m, [0] * m
for i in range(2, m):
    fac[i] = fac[i - 1] * i % mod
inv[-1] = pow(fac[-1], mod - 2, mod)
for i in range(m - 1, 0, -1):
    inv[i - 1] = inv[i] * i % mod

q = int(input())
ans_a = [0] * q
for pi in range(q):
    x, y = map(int, input().split())
    ans = 1
    for p in primes:
        if x % p == 0:
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            ans = ans * fac[cnt + y - 1] * inv[cnt] * inv[y - 1] % mod
    if x > 1:
        ans = ans * y % mod
    ans = ans * pow(2, y - 1, mod) % mod
    ans_a[pi] = ans

print(*ans_a, sep='\n')
