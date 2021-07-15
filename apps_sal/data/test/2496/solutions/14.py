n = int(input())
A = list(map(int, input().split()))

maxV = (10 ** 6 + 1)

sieve = [i for i in range(maxV)]
p = 2

while p*p < maxV:
    if sieve[p] == p:
        for q in range(p*2, maxV, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

from math import gcd

g = 0
primes = set()
for a in A:
    g = gcd(g, a)

    v = a


if g > 1:
    print('not coprime')
    return

for a in A:
    temp_prime = set()
    while a > 1:
        prime = sieve[a]
        temp_prime.add(prime)
        a = a // prime

    for t in temp_prime:
        if t in primes:
            print('setwise coprime')
            return
        primes.add(t)

print('pairwise coprime')
