import sys
X, Y = map(int, input().split())
if (X + Y) % 3 != 0:
    print(0)
    return
turn = (X + Y) // 3
X -= turn
Y -= turn

if X < 0 or Y < 0:
    print(0)
    return


def nCr(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
size = 10**6  # size >= n
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, size + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

print(nCr(X + Y, X, mod))
