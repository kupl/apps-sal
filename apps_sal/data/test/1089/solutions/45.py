import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 18
eps = 10 ** (-7)
(m, n, k) = list(map(int, readline().split()))


def comb(n, r, mod):
    r = min(r, n - r)
    mol = 1
    deno = 1
    for i in range(1, r + 1):
        mol = mol * (n - r + i) % mod
        deno = deno * i % mod
    ret = mol * pow(deno, mod - 2, mod) % mod
    return ret


def f1(x, y, a, b):
    return (a + b - x - y) * (a - x + 1) * (b - y + 1) // 2


def f2(x, a):
    return (a - x) * (a - x + 1) // 2


ans = 0
for x in range(1, n + 1):
    for y in range(1, m + 1):
        a = n - x + 1
        b = m - y + 1
        c = m * (a * (a - 1) + x * (x - 1))
        d = n * (b * (b - 1) + y * (y - 1))
        ans += (c + d) // 2
        ans %= mod
ans = ans * comb(m * n - 2, k - 2, mod) % mod
ans = ans * pow(2, mod - 2, mod) % mod
print(ans)
