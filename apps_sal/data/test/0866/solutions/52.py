(x, y) = list(map(int, input().split()))


def nCr(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    a = b = 1
    for i in range(1, r + 1):
        a = a * n % mod
        b = b * i % mod
        n -= 1
    return a * pow(b, mod - 2, mod) % mod


z = x + y
if z % 3 != 0 or x - z // 3 < 0 or y - z // 3 < 0:
    print(0)
else:
    z //= 3
    print(nCr(z, min(x, y) - z))
