import sys


def comb(n, r, fact, revfact, mod):
    return fact[n] * revfact[n - r] * revfact[r] % mod


def solve():
    (H, W, A, B) = map(int, input().split())
    mod = 7 + 10 ** 9
    fact = [1] * (H + W + 4)
    revfact = [1] * (H + W + 4)
    for i in range(1, H + W + 4):
        fact[i] = i * fact[i - 1] % mod
    revfact[H + W + 3] = pow(fact[H + W + 3], mod - 2, mod)
    for i in reversed(range(1, H + W + 3)):
        revfact[i] = (i + 1) * revfact[i + 1] % mod
    ans = 0
    for j in range(B + 1, W + 1):
        up = comb(H - A + j - 2, j - 1, fact, revfact, mod)
        down = comb(A + W - j - 1, A - 1, fact, revfact, mod)
        ans += up * down % mod
        ans %= mod
    print(ans)
    return 0


def __starting_point():
    solve()


__starting_point()
