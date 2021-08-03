def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
N, K = list(map(int, input().split()))
n = N * 2
r = min(N, K + 1)
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

ans = 0
for i in range(r):
    ans += cmb(N, i, mod) * cmb(N - 1, i, mod)
if K == 1:
    ans -= 1
print((ans % mod))
