def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 10**4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
N, K = map(int, input().split())
mod = 10**9 + 7
ans = 0
k = N - K
for i in range(K):
    ans = cmb(N - K + 1, i + 1, mod) * cmb(K - 1, i, mod)
    print(ans % mod)
