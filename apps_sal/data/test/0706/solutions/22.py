def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


mod = 10 ** 9 + 7
a, b, n, x = map(int, input().split())
ans = (pow(a, n, mod) * x % mod) % mod
if a != 1:
    ans2 = ((b * (pow(a, n, mod) - 1) % mod) * modinv(a - 1, mod)) % mod
else:
    ans2 = (b * (n * a) % mod) % mod
print((ans + ans2) % mod)
