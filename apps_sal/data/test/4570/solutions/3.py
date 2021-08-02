# 数値の取得
N, A, B = map(int, input().split())

# 料金の最安値を出力
plan1 = A * N
plan2 = B
print(min(plan1, plan2))
