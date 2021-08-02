import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

n_ = 2 * 10**6 + 5
mod = 10**9 + 7
fun = [1] * (n_ + 1)
for i in range(1, n_ + 1):
    fun[i] = fun[i - 1] * i % mod
rev = [1] * (n_ + 1)
rev[n_] = pow(fun[n_], mod - 2, mod)
for i in range(n_ - 1, 0, -1):
    rev[i] = rev[i + 1] * (i + 1) % mod


def nCr(n, r):
    if r > n:
        return 0
    return fun[n] * rev[r] % mod * rev[n - r] % mod


def modinv(x, mod):
    a, b = x, mod
    u, v = 1, 0
    while b:
        t = a // b
        a -= t * b; a, b = b, a
        u -= t * v; u, v = v, u
    return u % mod


inv26 = modinv(26, mod)


def solve():
    k = ni()
    s = ns()
    n = len(s)
    ans = 0
    v = 1
    u = pow(26, k, mod)
    for i in range(n, n + k + 1):
        ans = (ans + nCr(i - 1, n - 1) * v * u) % mod
        u = u * inv26 % mod
        v = v * 25 % mod
    print(ans)
    return


solve()
