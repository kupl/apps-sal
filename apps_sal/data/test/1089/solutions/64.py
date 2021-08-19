(n, m, k) = map(int, input().split())
mod = 10 ** 9 + 7
cum_n = 0
t = 0
for i in range(1, n):
    t += i
    cum_n += t
cum_m = 0
t = 0
for i in range(1, m):
    t += i
    cum_m += t
ans = (cum_n * m ** 2 + cum_m * n ** 2) % mod


def nCr(n, r, mod=10 ** 9 + 7):
    r = min(n - r, r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n + 1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


if n * m - 2 == 0:
    p = 1
else:
    p = nCr(n * m - 2, k - 2)
ans = ans * p % mod
print(ans)
