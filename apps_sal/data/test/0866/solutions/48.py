x, y = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


def knight(x, y):
    s = (0, 0)
    if x == y == 0:
        return 0
    if (x + y) % 3:
        return 0
    if (2 * y - x) % 3 or (2 * x - y) % 3:
        return 0

    a, b = (2 * y - x) // 3, (2 * x - y) // 3
    n = (x + y) // 3
    r = min(a, b)

    if a < 0 or b < 0:
        return 0

    return cmb(n, r, mod)


print(knight(x, y))
