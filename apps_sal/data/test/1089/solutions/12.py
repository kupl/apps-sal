(n, m, k) = map(int, input().split())
n_ = n * m
mod = 10 ** 9 + 7
fun = [1] * (n_ + 1)
for i in range(1, n_ + 1):
    fun[i] = fun[i - 1] * i % mod
rev = [1] * (n_ + 1)
rev[n_] = pow(fun[n_], mod - 2, mod)
for i in range(n_ - 1, 0, -1):
    rev[i] = rev[i + 1] * (i + 1) % mod


def nCr(n, r):
    if r > n:
        return 0
    return fun[n] * rev[r] % mod * rev[n - r] % mod


x = sum((i * (n - i) for i in range(n))) % mod
y = sum((i * (m - i) for i in range(m))) % mod
ans = (x * m ** 2 + y * n ** 2) % mod * nCr(n * m - 2, k - 2) % mod
print(ans)
