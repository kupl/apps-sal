r1, c1, r2, c2 = list(map(int, input().split()))
mod = 10 ** 9 + 7


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * pow(g1[r], mod - 2, mod) * pow(g1[n - r], mod - 2, mod) % mod


def make_table(n, mod=10 ** 9 + 7):
    N = n
    # 元テーブル
    g1 = [0] * (N + 1)
    g1[0] = 1
    g1[1] = 1

    tmp = g1[1]
    for i in range(2, N + 1):
        tmp = tmp * i % mod
        g1[i] = (g1[i - 1] * i) % mod

    return g1


def f(x, y):
    return ((x + 2) * cmb(x + y + 2, y, mod) - y - 1) * pow(y + 1, mod - 2, mod)


g1 = make_table(2 * 10 ** 6 + 10)
answer = f(c2, r2) - f(c2, r1 - 1) - f(c1 - 1, r2) + f(c1 - 1, r1 - 1)
answer %= mod
print(answer)
