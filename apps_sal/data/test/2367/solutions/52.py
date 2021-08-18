def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 3 * 10 ** 5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


def __starting_point():
    H, W, A, B = list(map(int, input().split()))
    p = 10 ** 9 + 7
    ans = 0
    for i in range(H - A):
        if i == 0:
            ans += cmb(B + i, i, p) * cmb(H + W - B - 2 - i, H - 1 - i, p)
            ans %= p
        else:
            ans += cmb(B + i - 1, i, p) * cmb(H + W - B - 2 - i, H - 1 - i, p)
            ans %= p
    print(ans)


__starting_point()
