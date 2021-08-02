X, Y = map(int, input().split())
mod = 10**9 + 7


def nCk(n, k, p):
    fact = [1, 1] + [0] * (n - 1)
    inv = [0, 1] + [0] * (n - 1)
    factinv = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fact[i] = i * fact[i - 1] % p
        inv[i] = - inv[p % i] * (p // i) % p
        factinv[i] = factinv[i - 1] * inv[i] % p

    return fact[n] * factinv[k] * factinv[n - k] % p


ans = 0
if (X + Y) % 3 == 0 and X <= 2 * Y and Y <= 2 * X:
    a = (2 * Y - X) // 3
    b = (2 * X - Y) // 3
    ans = nCk(a + b, a, mod)
print(ans)
