import sys
readline = sys.stdin.readline
readall = sys.stdin.read


def ns():
    return readline().rstrip()


def ni():
    return int(readline().rstrip())


def nm():
    return map(int, readline().split())


def nl():
    return list(map(int, readline().split()))


def prn(x):
    return print(*x, sep='\n')


n_ = 5 * 10 ** 5
mod = 10 ** 9 + 7
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
    (a, b) = (x, mod)
    (u, v) = (1, 0)
    while b:
        t = a // b
        a -= t * b
        (a, b) = (b, a)
        u -= t * v
        (u, v) = (v, u)
    return u % mod


def solve():
    (n, m) = nm()
    s = 0
    v = 1
    for i in range(n + 1):
        s = (s + v * nCr(n, i) * nCr(m, i) * fun[i] % mod * (nCr(m - i, n - i) * fun[n - i] % mod) ** 2) % mod
        v *= -1
    print(s)
    return


solve()
