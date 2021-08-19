n, m, k = map(int, input().split())
mod = 998244353

N = 10**5 * 2  # N!まで求める
fact = [1, 1]  # 階乗の元テーブル
fact_inv = [1, 1]  # 階乗の逆元テーブル
inv = [0, 1]  # 逆元テーブル計算用テーブル 1,2,,...の逆元を求めてる

# 計算 O(1)


def comb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % mod

# 順列


def perm(n, r, mod):
    if (r < 0 or r > n):
        return 0
    return fact[n] * fact_inv[n - r] % mod


# 前処理 O(n)
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    fact_inv.append((fact_inv[-1] * inv[-1]) % mod)

ans = 0
for i in range(k + 1):
    ans += comb(n - 1, i, mod) * m * pow(m - 1, n - i - 1, mod)
    ans %= mod

print(ans)
