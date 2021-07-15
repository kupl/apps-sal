# 数値の取得
A,B,C,D = map(int,input().split())

# 面積の最大値を出力
AB = A * B
CD = C * D
print(max(AB,CD))
