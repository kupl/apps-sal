n = int(input())
# n個の入力値をリストに追加
p = []
for _ in range(0,n):
    p.append(int(input()))
# リストの合計からリスト中の最大値の1/2を引く
print(int(sum(p) - max(p) / 2))
