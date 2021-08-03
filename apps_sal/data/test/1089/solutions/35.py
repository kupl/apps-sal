N, M, K = map(int, input().split())

ans = 0
mod = 10**9 + 7


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(n, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N * M + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

coef = cmb(N * M - 2, K - 2, mod)

for i in range(1, N):
    ans += i * (N - i) * M * M

for j in range(1, M):
    ans += j * (M - j) * N * N

ans *= coef
ans %= mod
print(ans)
