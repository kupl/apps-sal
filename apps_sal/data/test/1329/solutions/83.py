from collections import defaultdict
primes = list(range(2, 101))
for i in range(len(primes)):
    if primes[i]:
        j = i
        j += primes[i]
        while j < len(primes):
            primes[j] = None
            j += primes[i]
primes = [p for p in primes if p]
N = int(input())
fact = defaultdict(int)
for p in primes:
    i = p
    while i <= N:
        fact[p] += N // i
        i *= p
f2 = set()
f4 = set()
f14 = set()
f24 = set()
f74 = set()
for p in fact:
    if fact[p] >= 2:
        f2.add(p)
    if fact[p] >= 4:
        f4.add(p)
    if fact[p] >= 14:
        f14.add(p)
    if fact[p] >= 24:
        f24.add(p)
    if fact[p] >= 74:
        f74.add(p)
ans = 0
ans += len(f74)
ans += len(f24) * (len(f2) - 1)
ans += len(f14) * (len(f4) - 1)
ans += (len(f2) - 2) * len(f4) * (len(f4) - 1) // 2
print(ans)
