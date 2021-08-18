from collections import defaultdict as dd
N = int(input())
A = [int(x) for x in input().split()]
Sieve = dd(lambda: 0)
for a in A:
    Sieve[a] += 1

ans, extra = 0, 0
for v in list(Sieve.values()):
    ans += 1
    if v > 1 and (v - 1) & 1:
        extra += 1
print((ans if not extra & 1 else ans - 1))
