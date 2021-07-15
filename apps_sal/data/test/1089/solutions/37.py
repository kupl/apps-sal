N, M, K = list(map(int, input().split()))

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
mod = 10 ** 9 + 7
n = 3 * 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
#一つの配置でK C 2本の線
#配置はMN C K 通り
#よって、MNCK * KC2 / MNC2 = (MN - 2)C(K - 2)回
#各2頂点間のコストは足される。
#答えは全ての2頂点間のコストの和 * (MN - 2)C(K - 2)

#全ての2頂点間のコストの和を求める
#距離 i 離れた二点の個数は (1 + 2 + ... N - i) * N
#つまり、N * (N - i + 1) * (N - i) / 2
#縦横あるので、 それぞれ足す
ans1 = 0
for i in range(1, M):
  ans1 += i * (M - i) % mod
  #print(ans1)
ans1 = (ans1 * N * N) % mod

ans2 = 0
for i in range(1, N):
  ans2 += i * (N - i) % mod
ans2 = (ans2 * M * M) % mod

#print(ans1, ans2)

ans = ans1 + ans2
print((ans * cmb(M * N - 2, K - 2, p) % mod))


