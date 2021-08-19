# 数値の取得
pnum = int(input())
plist = list()
for pcnt in range(0, pnum, 1):
    plist.append(int(input()))

# 合計金額を出力
half = max(plist) // 2
psum = sum(plist) - half
print(psum)
