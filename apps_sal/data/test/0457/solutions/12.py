from itertools import chain
from math import sqrt

ub = 10**5
ub_sqrt = int(sqrt(ub)) + 1
primes = {2, 3} | set(chain(list(range(5, ub, 6)), list(range(7, ub, 6))))
du = primes.difference_update
for n in chain(list(range(5, ub_sqrt, 6)), list(range(7, ub_sqrt, 6))):
    if n in primes:
        du(list(range(n * 3, ub, n * 2)))


x, n = list(map(int, input().split()))
divisors = []
for p in primes:
    if x % p == 0:
        divisors.append(p)
        while x % p == 0:
            x //= p
if x > 1:
    divisors.append(x)

ans = 1
mod = 10**9 + 7

for d in divisors:
    cur = d
    while cur <= n:
        ans = ans * pow(d, n // cur, mod) % mod
        cur *= d

print(ans)
