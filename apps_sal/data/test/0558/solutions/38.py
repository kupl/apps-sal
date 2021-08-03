import sys
def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())
mod = 998244353
n_max = 2 * (10**5 + 1)
F, FI = [0] * (n_max + 1), [0] * (n_max + 1)
F[0], FI[0] = 1, 1
for i in range(n_max):
    F[i + 1] = (F[i] * (i + 1)) % mod
FI[n_max - 1] = pow(F[n_max - 1], mod - 2, mod)
for i in reversed(range(n_max - 1)):
    FI[i] = (FI[i + 1] * (i + 1)) % mod


def comb(x, y):
    return (F[x] * FI[x - y] * FI[y]) % mod


P = [1]
for i in range(n):
    P.append((P[-1] * (m - 1)) % mod)

ans = 0
for i in range(k + 1):
    ans += m * P[n - 1 - i] * comb(n - 1, i)
    if ans > mod:
        ans %= mod
print(ans)
