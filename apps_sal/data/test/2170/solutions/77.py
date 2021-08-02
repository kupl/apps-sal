MAX = 5 * (10**5)
MOD = 10**9 + 7

_fact = [1, 1] + [0] * MAX
_inv = [0, 1] + [0] * MAX
_fact_inv = [1, 1] + [0] * MAX
for k in range(2, MAX + 1):
    _fact[k] = _fact[k - 1] * k % MOD
    _inv[k] = (-_inv[MOD % k] * (MOD // k)) % MOD
    _fact_inv[k] = _fact_inv[k - 1] * _inv[k] % MOD


def P(m, n):
    return _fact[m] * _fact_inv[m - n] % MOD


def C(m, n):
    return _fact[m] * _fact_inv[m - n] * _fact_inv[n] % MOD


def solve(n, m):
    res = 0
    for k in range(n + 1):
        sign = 1 - 2 * (k % 2)
        cur = sign * C(n, k) * P(m, k) * (P(m - k, n - k) ** 2)
        res = (res + cur) % MOD
    return res


n, m = map(int, input().split())
print(solve(n, m))
