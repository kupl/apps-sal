n, k = list(map(int, input().split()))
td = []
for _ in range(n):
    td.append(list(map(int, input().split())))
td.sort(key=lambda x: x[1], reverse=True)
td_core = []
td_sel = []
td_sub = []
cat = [0] * (n + 1)
for i in range(n):
    if i < k and cat[td[i][0]] == 0:
        td_core.append(td[i])
        cat[td[i][0]] = 1
    elif i < k:
        td_sel.append(td[i])
    elif cat[td[i][0]] == 0:
        td_sub.append(td[i])
        cat[td[i][0]] = 1
# i >= k and cat[td[i][0]]==1 となるものはすでにtd_core,td_sel,td_sub内ものと種類も被っている上に美味しさも低い
# 後の工程は種類を増やす処理なので、同じ種類のネタはそのネタの中で美味しさが最大のもの一つで十分。なので捨てる

# dの大きい順に貪欲にネタを取得したときの満足ポイント
kiso = sum([x[1] for x in td_core]) + sum([x[1] for x in td_sel])
bns = len(td_core)
ans = kiso + bns**2
# この状態からネタの種類を増やしていき最大が出てくるか検証
# td_sel内のネタは同一ネタが複数あり、そのネタ内で最大じゃないものが美味しさの大きい順に入っている。
# td_subにはtd_core,td_selにないネタの最大美味しさの寿司が入っている。
td_sel.sort(key=lambda x: x[1])
for i in range(min(len(td_sel), len(td_sub))):
    kiso -= td_sel[i][1]
    kiso += td_sub[i][1]
    bns += 1
    ans = max(ans, kiso + bns**2)
print(ans)
