from math import gcd
N = int(input())
A = list(map(int, input().split()))
MA = 10**6+10

g = 0
for a in A:
    g = gcd(g, a)
if g > 1:
    print('not coprime')
    return

sieve = [i for i in range(MA+1)]
p = 2
while p*p <= MA:
    if sieve[p] == p:
        for q in range(2*p, MA+1, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1
prim = set()
for a in A:
    tmp = set()
    while a > 1:
        tmp.add(sieve[a])
        a //= sieve[a]
    for t in tmp:
        if t in prim:
            print('setwise coprime')
            return
        prim.add(t)

print('pairwise coprime')

