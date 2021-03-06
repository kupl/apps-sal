from operator import mul
from functools import reduce


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
'\nin1 = kari1.split()\n'
in1 = input().split()
H = int(in1[0])
W = int(in1[1])
A = int(in1[2])
B = int(in1[3])
allCNT = 0
for idx1 in range(W - B):
    beforeCNT = cmb(H - A + B - 1 + idx1, H - A - 1, p)
    afterCNT = cmb(W + A - B - 2 - idx1, A - 1, p)
    allCNT = (allCNT + beforeCNT * afterCNT % p) % p
print(allCNT)
