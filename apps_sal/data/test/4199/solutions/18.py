n, k = map(int, input().split())
h = list(map(int, input().split()))
# ジェットコースターの乗れる人の数
able_num = 0
# リスト内の数字を取り出して、ｋより大きければ乗れる人をカウントアップ
for i in h:
    if i >= k:
        able_num += 1
print(able_num)
