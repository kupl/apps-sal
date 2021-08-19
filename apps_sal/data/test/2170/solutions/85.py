(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7
N = 10 ** 6
inv_t = [0] + [1]
for i in range(2, N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]
kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)


def cmb(n, r):
    return kai[n] * rev_kai[r] * rev_kai[n - r] % mod


def prm(n, r):
    return kai[n] * rev_kai[n - r] % mod


ans = 0
tmp = 1
for k in range(n + 1):
    ans += tmp * cmb(n, k) * prm(m - k, n - k) % mod
    ans %= mod
    tmp *= -1
ans *= prm(m, n)
ans %= mod
print(ans)
