# 解説見て書く

N, K = [int(x) for x in input().split()]
td = [0] * (N)
for i in range(N):
    td[i] = [int(x) for x in input().split()]

# ネタ種類降順でソート
# 同じネタの中ではおいしいものから順に並ぶ
td = sorted(td, reverse = True)

var_p1 = [0] * N   # 種類数を増やす寿司のリスト
var_p0 = [0] * N   # 種類数を増やさない寿司のリスト

n_p1 = 0
n_p0 = 0
for i in range(N):
    if i == 0 or (i > 0 and td[i][0] != td[i - 1][0]):  # 種類が変わる
        var_p1[n_p1] = td[i][1]  # おいしさを追加
        n_p1 += 1
    else:
        var_p0[n_p0] = td[i][1]  # おいしさを追加
        n_p0 += 1

var_p1.sort(reverse = True)
var_p0.sort(reverse = True)

val_taste = sum(var_p0[0 : K])
val_vars = 0
ans = 0

for j in range(1, K + 1):  # 種類数1〜Kを試す
    val = var_p1[j - 1]
    if val <= 0: break  # これ以上種類を増やせない
    # var_p1からn_p1個選び、var_p0からK - n_p1個選ぶ
    val_taste = val_taste + val - var_p0[K - j]
    val_vars = j * j
    ans = max(ans, val_taste + val_vars)

print(ans)
