# 3つの整数 A, B, C が与えられます。
# 整数 C が A 以上 かつ B 以下であるかを判定してください。

# 制約
# −100 ≦ A, B, C ≦ 100
# A, B, C は全て整数

# 標準入力から A, B, C を取得する
a, b, c = list(map(int, input().split()))

# 判定して結果を出力する
resut = "ret"

if a <= c and b >= c:
    result = "Yes"
else:
    result = "No"

print(result)

