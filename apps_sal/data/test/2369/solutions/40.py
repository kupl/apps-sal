import math


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
N = 10**5 + 5
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

N, K = list(map(int, input().split()))
A = sorted(tuple(map(int, input().split())))
B = tuple(A[i + 1] - A[i] for i in range(len(A) - 1))
lim = math.ceil(len(B) / 2)

L = 10**9 + 7
ans = 0
multi = cmb(N, K, mod)
for j in range(lim):
    front = j + 1
    back = N - front
    tmp_b = 0
    tmp_f = 0
    if front >= K:
        tmp_f = cmb(front, K, mod)
    if back >= K:
        tmp_b = cmb(back, K, mod)
    if j == (len(B) - 1) / 2:
        ans += (multi - tmp_b - tmp_f) * (B[j]) % L
    else:
        ans += (multi - tmp_b - tmp_f) * (B[j] + B[len(B) - 1 - j]) % L
print(ans % L)
