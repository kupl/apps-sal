k = 2 * 10**5
mod = 10**9 + 7

n, a, b = map(int, input().split())

modinv_table = [-1] * (k + 1)
for i in range(1, k + 1):
    modinv_table[i] = pow(i, -1, mod)


def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


print((pow(2, n, mod) - binomial_coefficients(n, a) - binomial_coefficients(n, b) - 1) % mod)
