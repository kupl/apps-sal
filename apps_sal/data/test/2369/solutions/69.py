from functools import lru_cache
n, k = list(map(int, input().split()))
A = sorted(map(int, input().split()))
mod = 10 ** 9 + 7
# 階乗とその逆元の計算
factrial = [0 for _ in range(n + 1)]
factrial[0] = 1
for i in range(1, n + 1):
    factrial[i] = (factrial[i - 1] * i) % mod
inverse_factrial = list()
for f in factrial:
    inverse_factrial.append(pow(f, -1, mod))


@lru_cache(maxsize=None)
def nCr(n, r):
    return (factrial[n] * inverse_factrial[r] * inverse_factrial[n - r]) % mod


ans = 0
# 最大値の和
for i, a in enumerate(A[k - 1:], k - 1):
    ans += ((a % mod) * nCr(i, k - 1)) % mod
    ans %= mod
# 最小値の和
A.reverse()
for i, a in enumerate(A[k - 1:], k - 1):
    ans -= ((a % mod) * nCr(i, k - 1)) % mod
    ans %= mod
print(ans)
