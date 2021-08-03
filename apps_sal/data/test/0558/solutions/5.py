
def pre_combi1(n, p):
    fact = [1] * (n + 1)  # fact[n] = (n! mod p)
    factinv = [1] * (n + 1)  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0] * (n + 1)  # factinv 計算用
    inv[1] = 1
    # 前処理
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % p
        inv[i] = -inv[p % i] * (p // i) % p
        factinv[i] = factinv[i - 1] * inv[i] % p
    return fact, factinv


def combi1(n, r, p, fact, factinv):
    """
    k<n<10**7でpが素数のときのnCr % pを求める
    """
    # 本処理
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 998244353
fact, finv = pre_combi1(2 * 10**5 + 1, p)
n, m, k = map(int, input().split())
ans = 0
dup = [0] * n
dup[0] = 1
for j in range(1, n):
    dup[j] = dup[j - 1] * (m - 1) % p
for i in range(k + 1):
    ans += m * combi1(n - 1, i, p, fact, finv) * dup[n - i - 1]
    ans %= p
print(ans)
