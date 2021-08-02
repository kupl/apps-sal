from bisect import bisect
from sys import stdin
_data = iter(stdin.read().split('\n'))
def input(): return next(_data)


V = 210000
primes = []
is_prime = [True] * V
is_prime[0] = False
is_prime[1] = False
for i in range(2, V):
    if is_prime[i]:
        primes.append(i)
        for j in range(i + i, V, i):
            is_prime[j] = False

n = int(input())
a = list(map(int, input().split()))
ra = [0] * n
for i in range(n):
    a[i] -= 1
    ra[a[i]] = i

buf = []
p = 0
while p < n:
    while ra[p] != p:
        d = ra[p] - p + 1
        d = primes[bisect(primes, d) - 1] - 1
        r = ra[p]
        q = r - d
        ra[a[q]], ra[a[r]] = ra[a[r]], ra[a[q]]
        a[q], a[r] = a[r], a[q]
        buf.append('{} {}'.format(q + 1, r + 1))
    p += 1
print(len(buf))
print('\n'.join(buf))
