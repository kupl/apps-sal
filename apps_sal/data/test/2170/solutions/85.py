n, m = list(map(int, input().split()))

mod = 10 ** 9 + 7
N = 10 ** 6

#逆元テーブル
inv_t = [0]+[1]
for i in range(2, N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

#階乗計算
kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)

# コンビネーション計算
def cmb(n, r):
    return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

def prm(n, r):
    return kai[n] * rev_kai[n-r] % mod

ans = 0
tmp = 1

# 包除原理に従って場合の数を求める
for k in range(n+1):
    #　!(Ai != Bi)、つまり　Ai == Bi　という条件N個からK個選び
    # それらの条件の「かつ」の条件を満たす場合の数考える
    ans += tmp * cmb(n, k) * prm(m-k, n-k) % mod # KはAと一致するように決めて、残りのN-K箇所を自由に決める
    ans %= mod
    tmp *= -1

# Aの選び方をかける
ans *= prm(m, n)
ans %= mod

print(ans)


