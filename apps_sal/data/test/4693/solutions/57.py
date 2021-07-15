# 二つの整数 A, Bが入力されます。
# A + B の値を出力してください。
# ただし、
# A + B が 10 以上の場合は、
# 代わりに error と出力してください。

# 制約
# A, B は整数である。
# 1 ≦ A, B ≦ 9

# 標準入力から A, B の値を取得する
a, b = list(map(int, input().split()))

# 計算結果を出力する
result = "error"

if a + b < 10:
    result = a + b

print(result)

