n, k = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))


def solve(n, k, As, Bs):
    mod = 10 ** 9 + 7
    c = 1
    for a, b in zip(As, Bs):
        c *= f(a, b, k, mod)
        c %= mod
    return c


def f(a, b, k, mod):
    total = (10 ** k - 1) // a + 1
    p = ((b + 1) * (10 ** (k - 1)) - 1) // a
    q = (b * (10 ** (k - 1)) - 1) // a
    return (total - p + q) % mod


print(solve(n, k, As, Bs))
