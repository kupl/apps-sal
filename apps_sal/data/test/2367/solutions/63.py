# 縦H A

def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
N = (10**5) * 2
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
H, W, A, B = list(map(int, input().split()))
ans = 0
for i in range(H - A):
    ans += cmb(B + i - 1, B - 1, mod) * cmb(H - i + W - B - 2, W - B - 1, mod)
print((ans % mod))
# 1 1 1
# $ 1 2
