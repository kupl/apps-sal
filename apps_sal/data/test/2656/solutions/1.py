k = int(input())
s = input()
s = len(s)
mod = 10 ** 9 + 7
n = k + s


def _fac_inv(_n, _mod):
    _fac = [1] * (_n + 1)
    _inv = [1] * (_n + 1)
    for i in range(_n):
        _fac[i + 1] = _fac[i] * (i + 1) % _mod
    _inv[_n] = pow(_fac[_n], _mod - 2, _mod)
    for i in range(_n, 0, -1):
        _inv[i - 1] = _inv[i] * i % _mod
    return (_fac, _inv)


(fac, inv) = _fac_inv(n, mod)
n25 = [1]
n26 = [1]
for _ in range(n - s):
    n25.append(n25[-1] * 25 % mod)
    n26.append(n26[-1] * 26 % mod)
ans = 0
for i in range(s, n + 1):
    ans = (ans + fac[i - 1] * inv[s - 1] * inv[i - s] * n25[i - s] * n26[n - i]) % mod
print(ans)
