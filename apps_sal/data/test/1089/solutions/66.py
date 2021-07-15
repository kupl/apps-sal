from functools import reduce
n, m, k = list(map(int, input().split()))
mod = 10**9 + 7


def nCr(n, r, MOD=10**9 + 7):
    from functools import reduce
    if r == 0:
        return 1
    num = reduce(lambda x, y: x * y % MOD, list(range(n, n - r, -1)))
    den = reduce(lambda x, y: x * y % MOD, list(range(1, r + 1)))
    return num * pow(den, MOD - 2, MOD) % MOD


ncr = nCr(n * m - 2, k - 2)
ans = 0
for d in range(1, m):
    temp = d * (m - d) * n**2
    temp %= mod
    ans += temp
    ans %= mod
for d in range(1, n):
    temp = d * (n - d) * m**2
    temp %= mod
    ans += temp
    ans %= mod
ans *= ncr
ans %= mod
print(ans)

