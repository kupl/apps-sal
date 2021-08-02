M = 1000000007
r1, c1, r2, c2 = map(int, input().split())
n = r2 + c2 + 2
fac = [1] + [0] * n
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % M


def f(r, c): return fac[r + c + 2] * pow(fac[c + 1], M - 2, M) * pow(fac[r + 1], M - 2, M) - 1


print((f(r2, c2) - f(r2, c1 - 1) - f(r1 - 1, c2) + f(r1 - 1, c1 - 1)) % M)
