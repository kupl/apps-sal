P = 10 ** 9 + 7
fac = [1]
ifac = [1]
ff = 1
for i in range(1, 200001):
    ff *= i
    ff %= P
    fac.append(ff)
    ifac.append(pow(ff, P - 2, P))


def ncr(n, r):
    return fac[n] * ifac[r] % P * ifac[n - r] % P


(h, w, a, b) = list(map(int, input().split()))
s = 0
nC = b - 1
kC = 0
nD = w - b - 1 + h - 1
kD = h - 1
for i in range(h - a):
    C = ncr(nC, kC)
    D = ncr(nD, kD)
    s = (s + C * D) % P
    nC += 1
    kC += 1
    kD -= 1
    nD -= 1
print(s)
