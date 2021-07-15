# 上皿天秤は、左の皿に乗っているおもりの重さの合計を L とし、
# 右の皿に乗っているおもりの重さの合計を R としたとき、
# L > R なら左に傾き、 L = R なら釣り合い、
# L < R なら右に傾きます。
#
# 高橋君は、上皿天秤の左の皿に重さ A のおもりと重さ B のおもりを、
# 右の皿に重さ C のおもりと重さ D のおもりを置きました。
#
# 上皿天秤が左に傾くなら Left を、
# 釣り合うなら Balanced を、
# 右に傾くなら Right を出力してください。

# 制約
# 1 ≦ A, B, C, D ≦ 10
# 入力はすべて整数である

# 標準入力から A, B, C ,D の値を取得する
a, b, c, d = list(map(int, input().split()))

# 上皿天秤の状態を判定し、結果を出力する
result = "ret"

if (a + b) > (c + d):
    result = "Left"
elif (a + b) < (c + d):
    result = "Right"
else:
    result = "Balanced"

print(result)

