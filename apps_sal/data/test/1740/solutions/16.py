n = int(input())

# 要素iの親（マージ先）を指す
parent = [i for i in range(n + 1)]

# 各要素をここにマージしていく
group = [[i] for i in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    # xのマージ先の配列の要素数 >= yのマージ先の配列の要素数となるようにxとyを入れ替える（マージテクの前処理）
    if len(group[parent[x]]) < len(group[parent[y]]):
        x, y = y, x

    # 要素数が大きい方へマージする（マージテク）
    group[parent[x]] += group[parent[y]]

    # マージされた各要素の親（マージ先）の情報を更新する
    for j in group[parent[y]]:
        parent[j] = parent[x]

print(*group[parent[1]])
