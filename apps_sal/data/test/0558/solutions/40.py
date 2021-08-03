n, m, k = list(map(int, input().split()))

MOD = 998244353
fact = [1] * (n + 1)  # 階乗を格納するリスト
factinv = [1] * (n + 1)  # 階乗を格納するリスト
for i in range(n):
    fact[i + 1] = fact[i] * (i + 1) % MOD  # 階乗を計算
    factinv[i + 1] = pow(fact[i + 1], MOD - 2, MOD)  # MODを法とした逆元（フェルマーの小定理）


def nCk(n, k):  # 組み合わせ(MOD)を返却する
    return fact[n] * factinv[n - k] * factinv[k] % MOD


ans = 0
for i in range(k + 1):
    ans += m * pow(m - 1, n - 1 - i, MOD) * nCk(n - 1, i) % MOD

print((ans % MOD))
