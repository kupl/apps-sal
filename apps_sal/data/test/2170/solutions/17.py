M = 10**9 + 7
n, m = map(int, input().split())
F = [1]
for i in range(1, m + 1):
    F += [i * F[-1] % M]
a = 0
for k in range(n + 1):
    a += (-1)**k * F[m - k] * pow(F[k] * F[n - k], -1, M) % M
print(a * F[n] * F[m] * pow(F[m - n]**2, -1, M) % M)
