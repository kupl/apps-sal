n, m, k = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
N = 3 * 10**5
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

xans, yans = 0, 0
for i in range(1, n):
    xans += i * cmb(n * m - 2, k - 2, mod) * (n - i) * m**2 % mod
for i in range(1, m):
    yans += i * cmb(n * m - 2, k - 2, mod) * (m - i) * n**2 % mod
print((xans + yans) % mod)
