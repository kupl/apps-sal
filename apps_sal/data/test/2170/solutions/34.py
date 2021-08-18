def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 5 * 10**5
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

N, M = map(int, input().split())
ans = 0
for i in range(N + 1):
    ans += cmb(N, i, mod) * ((-1)**i) * g1[M] * g2[M - i] * ((g1[M - i] * g2[M - N])**2)
    ans %= mod
print(ans)
