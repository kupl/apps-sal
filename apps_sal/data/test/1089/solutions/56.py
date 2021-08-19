import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#mod = 998244353
INF = 10**18
eps = 10**-7

m, n, k = list(map(int, readline().split()))


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
        ans += f1(x, y, n, m) + f1(1, 1, x, y) + f1(1, y, x, m) + f1(x, 1, n, y)
        ans -= f2(x, n) + f2(1, x) + f2(1, y) + f2(y, m)
        ans %= mod

ans = (ans * comb(m * n - 2, k - 2, mod)) % mod
ans = ans * pow(2, mod - 2, mod) % mod

print(ans)
