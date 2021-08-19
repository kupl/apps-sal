n, k, *a = map(int, open(0).read().split())
d = [0] * 41  # aの各桁の1の数の和
for i in range(n):
    for j in range(41):
        d[j] += (a[i] >> j) & 1
f = 0
la = len(bin(max(a))) - 2  # max(a)の桁数
lk = len(bin(k)) - 2  # kの桁数
b = [0] * 41  # 最適なX
# k以下の数で上桁からみる,kが1でXが0となったときXはそれより下桁は自由にとれる
# 各桁1と0どちらが多いかでXの各桁を決める
for i in range(lk - 1, -1, -1):
    if (k >> i) & 1 == 1:
        if d[i] < n - d[i]:
            b[i] = 1
        else:
            b[i] = 0
            f = 1
    if (k >> i) & 1 == 0:
        if d[i] < n - d[i] and f == 1:
            b[i] = 1
        else:
            b[i] = 0
ans = 0
# 答えはXの各桁の数,ではない方の数の個数の和
for i in range(max(lk, la)):
    ans += (1 << i) * [d[i], n - d[i]][b[i]]
print(ans)
