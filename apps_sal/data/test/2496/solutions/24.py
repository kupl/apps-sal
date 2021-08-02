from math import gcd
from functools import reduce

N, *A = list(map(int, open(0).read().split()))

t = [0] * (10 ** 6 + 1)
for a in A:
    t[a] += 1

for i in range(2, 10 ** 6 + 1):
    c = 0
    for j in range(i, 10 ** 6 + 1, i):
        c += t[j]
    if c > 1:
        break
else:
    print('pairwise coprime')
    return

if reduce(gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')
