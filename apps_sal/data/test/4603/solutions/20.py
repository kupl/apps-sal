# 数値の取得
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 料金の最安値を出力
train = min(A, B)
bus = min(C, D)
tbsum = train + bus
print(tbsum)
