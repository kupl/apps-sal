
N = int(input())
a = list(map(int, input().split()))
sa = []
c = [0] * 4
ans = 'No'

# 4で割った余り一覧表作成
for i in a:
    sa.append(i % 4)

for i in sa:
    c[i] += 1

# 2の倍数がない時、奇数の数の和が4の倍数の個数+1以下ならOK
if c[2] == 0:
    if c[1] + c[3] <= c[0] + 1:
        ans = 'Yes'
# 2の倍数がある時、まとめて端に寄せて、奇数個でも偶数個でも奇数1個分の扱いになる
# よって奇数の数の和が4の倍数の個数以下であればOK
else:
    if c[1] + c[3] <= c[0]:
        ans = 'Yes'

# print(c)
print(ans)
