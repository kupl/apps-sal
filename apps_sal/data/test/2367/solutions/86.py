from math import comb
h, w, a, b = list(map(int, input().split()))
s = 0
nC = b - 1
kC = 0
nD = w - b - 1 + h - 1
kD = h - 1
p = 1000000007
fac = [1]
ff = 1
for i in range(1, 200001):
    ff *= i
    ff %= p
    fac.append(ff)


def ncr(n, r, p):
    return (fac[n] * pow(fac[r], p - 2, p) % p * pow(fac[n - r], p - 2, p) % p)


for i in range(h - a):
    C = ncr(nC, kC, 1000000007)
    D = ncr(nD, kD, 1000000007)
    s = (s + C * D) % 1000000007
    nC += 1
    kC += 1
    kD -= 1
    nD -= 1
print(s)
