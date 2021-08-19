(n, m) = map(int, input().split())
mod = 998244353
n_max = 2 * (10 ** 5 + 1)
(F, FI) = ([0] * (n_max + 1), [0] * (n_max + 1))
(F[0], FI[0]) = (1, 1)
for i in range(n_max):
    F[i + 1] = F[i] * (i + 1) % mod
FI[n_max - 1] = pow(F[n_max - 1], mod - 2, mod)
for i in reversed(range(n_max - 1)):
    FI[i] = FI[i + 1] * (i + 1) % mod


def comb(x, y):
    return F[x] * FI[x - y] * FI[y] % mod


print(comb(m, n - 1) * (n - 2) * pow(2, n - 3, mod) % mod)
