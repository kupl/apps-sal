import sys


def input():
    return sys.stdin.readline().rstrip()


mod = 10 ** 9 + 7


def make_tables(n, mod=10 ** 9 + 7):
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fac.append(fac[-1] * i % mod)
        inv.append((mod - inv[mod % i] * (mod // i)) % mod)
        finv.append(finv[-1] * inv[-1] % mod)
    return (fac, finv)


def nCk(n, k, mod=10 ** 9 + 7):
    k = min(k, n - k)
    return fac[n] * finv[k] * finv[n - k] % mod


(n, m, k) = list(map(int, input().split()))
(fac, finv) = make_tables(n * m - 2)
ans = 0
for i in range(1, m):
    ans += i * n * n * (m - i) * nCk(n * m - 2, k - 2)
    ans %= mod
for j in range(1, n):
    ans += j * m * m * (n - j) * nCk(n * m - 2, k - 2)
    ans %= mod
print(ans)
