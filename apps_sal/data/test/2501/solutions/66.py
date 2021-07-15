# 参考 : https://atcoder.jp/contests/abc166/submissions/16829140
n = int(input())
a = list(map(int,input().split()))
# 参加者 i,j が取引する場合、 j - i = A_i + A_j が成り立つ。
# 変形すると -i - A_i = -j + A_j, i + A_i = j - A_j になる。
# l = i + A_i, r = j - A_j
l = [i + a[i] for i in range(n)]
r = [i - a[i] for i in range(n)]
# 連想配列(辞書)を使う。
x = {}
y = {}
# 辞書にキーを追加する。
for i in range(n):
    x[l[i]] = 0
    y[l[i]] = 0
    y[r[i]] = 0
# キーの値を人数分増やす。
for i in range(n):
    x[l[i]] += 1
    y[r[i]] += 1
ans = 0
# x のキーで取引する人数を調べる。
for i in set(x.keys()):
    ans += x[i] * y[i]
print(ans)
