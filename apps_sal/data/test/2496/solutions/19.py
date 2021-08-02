from functools import reduce
from math import gcd

P = [0, 0] + list(range(2, 1000))
for i in range(32):
    if P[i] == 0: continue
    P[2 * i::i] = [0] * (-2 - -1000 // i)
P = [p for p in P if p]

N = int(input())
A = [a for a in map(int, input().split()) if a > 1]
i = N - len(A)

# N <= 78498

z = set()
y = 0
for a in A:
    x = 0
    for p in P:
        while a % p == 0:
            a //= p
            x |= 1
        x <<= 1
    if y & x: break
    y |= x
    if a > 1:
        if a in z: break
        z.add(a)
else:
    print("pairwise coprime")
    return

if i or reduce(gcd, A) == 1: print("setwise coprime")
else: print("not coprime")
