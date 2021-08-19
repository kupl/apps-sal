H, W, A, B = map(int, input().split())
mod = 10**9 + 7

F = [1] * 200010
p = 1
for i in range(1, len(F)):
    F[i] = p = p * i % mod


def comb(n, k):
    return F[n] * pow(F[n - k], mod - 2, mod) * pow(F[k], mod - 2, mod) % mod


ans = 0
for h in range(H - A):
    x = comb(B - 1 + h, h)  # 右にB-1回、下にh回移動する方法の数
    y = comb(W + H - B - h - 2, H - h - 1)  # 右にW-B-1回、下にH-h-1回移動する方法の数
    ans += x * y
    ans %= mod
print(ans)
