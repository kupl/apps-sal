import random

n = int(input())
a = list(map(int, input().split()))


def add(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            primes.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        primes.add(x)


ans = float('inf')
primes = {2}

for x in random.choices(a, k=min(n, 8)):
    for dx in range(-1, 2):
        add(x + dx)

for p in primes:
    cand = 0
    for x in a:
        if x < p:
            cand += p - x
        else:
            r = x % p
            cand += min(r, p - r)

    ans = min(ans, cand)
    if ans == 0:
        break

print(ans)
