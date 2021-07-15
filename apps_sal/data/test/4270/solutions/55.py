# Nを取得
N = int(input())

# vを取得
v = list(map(int, input().split()))

# vを昇順ソート
v = sorted(v)

# result = v[0] vの小さい値から1つ選ぶ
result = v[0]

# vの2番目の値と平均をとる。これを4番目〜N番目 result = (results + v[i]) / 2
for i in range(1, len(v)):
    result = (result + v[i]) / 2

# 結果出力
print(result)
