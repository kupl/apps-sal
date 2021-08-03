# コンビネーション
mod = 10**9 + 7


def cmb(n, r, mod=mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


NN = 10**5  # 使うデータによって変える
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, NN + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


N, K = map(int, input().split())

for i in range(1, K + 1):
    ans = cmb(K - 1, K - i) * cmb(N - K + 1, N - K - i + 1) % mod
    print(ans)
