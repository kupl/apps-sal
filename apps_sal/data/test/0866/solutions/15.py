# https://atcoder.jp/contests/abc145/tasks/abc145_d
MOD = 10**9 + 7
x, y = list(map(int, input().split()))

if (x + y) % 3 != 0:
  print((0))
  return

# https://qiita.com/derodero24/items/91b6468e66923a87f39f#%E7%95%AA%E5%A4%96%E7%B7%A8


def cmb(n, r):
  if (r < 0 or r > n):
    return 0
  r = min(r, n - r)
  return g1[n] * g2[r] * g2[n - r] % MOD


N = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
  g1.append((g1[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
  g2.append((g2[-1] * inverse[-1]) % MOD)

print((cmb((x + y) // 3, x - (x + y) // 3)))

