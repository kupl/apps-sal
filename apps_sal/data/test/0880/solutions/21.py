def iterative_egcd(a, b):
    (x, y, u, v) = (0, 1, 1, 0)
    while a != 0:
        (q, r) = (b // a, b % a)
        (m, n) = (x - u * q, y - v * q)
        (b, a, x, y, u, v) = (a, r, u, v, m, n)
    return (b, x, y)


def modinv(a, m):
    (g, x, y) = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def factorialMod(n, modulus):
    ans = 1
    if n <= modulus // 2:
        for i in range(1, n + 1):
            ans = ans * i % modulus
    else:
        for i in range(1, modulus - n):
            ans = ans * i % modulus
        ans = modinv(ans, modulus)
        if n % 2 == 0:
            ans = -1 * ans + modulus
    return ans % modulus


n = int(input())
if n == 1:
    print(1)
else:
    m = 998244353
    ans = (n - 1) * factorialMod(n, m) % m
    k = 0
    for i in range(3, n + 1):
        k = (k + 1) * i % m
    print((ans - k) % m)
