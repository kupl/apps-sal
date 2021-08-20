mod = 10 ** 9 + 7
n = 10 ** 6
inv_t = [0] + [1]
for i in range(2, n):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]
kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, n):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)


def cmb(n, r):
    return kai[n] * rev_kai[r] * rev_kai[n - r] % mod


def prm(n, r):
    return kai[n] * rev_kai[n - r] % mod


(N, M) = map(int, input().split())


def f(x):
    e = cmb(N, x) * prm(M, x) * prm(M - x, N - x) * prm(M - x, N - x)
    e %= mod
    return e


ans = 0
for i in range(N + 1):
    g = f(i) * (-1) ** i
    ans += g
print(ans % mod)
