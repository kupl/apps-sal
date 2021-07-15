h, w, a, b = map(int, input().split())
mod = 10 ** 9 + 7
n = h + w

f = [1 for _ in range(n)]
f_inv = [1 for _ in range(n)]
for i in range(1, n):
    f[i] = f[i-1] * i % mod
    f_inv[i] = pow(f[i], mod-2, mod)


def comb(n, k):
    return (f[n] * f_inv[k] % mod) * f_inv[n-k] % mod

ans = comb(h+w-2, h-1)
for i in range(b):
    ans -= comb(h-a+i-1, i) * comb(a+w-i-2, a-1) % mod
    ans %= mod

print(ans)
