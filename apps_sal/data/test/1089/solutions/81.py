N, M, K = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
MAX_N = 10**6  # N >= n
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, MAX_N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

k = cmb(M * N - 2, K - 2, mod)


def calc(p, q, d):
    return d * (p - d) * (q ** 2)


ans = 0

for i in range(N):
    ans += calc(N, M, i)
for i in range(M):
    ans += calc(M, N, i)

ans %= mod

ans *= k

ans %= mod

print(ans)
