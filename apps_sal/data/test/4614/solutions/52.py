# 3 つの整数 A, B, Cが与えられます。
# A, B, C のうち 2つは 同じ整数であり、
# 残りの 1つだけ異なる整数です。
# 例えば、A = 5, B = 7, C = 5の場合、
# A, C の 2つは同じ整数であり、
# B は 1つだけ異なる整数です。
# 3つの整数のうち、1つだけ異なる整数を求めてください。

# 制約
# -100 ≦ A, B, C ≦ 100
# A, B, C は整数
# 入力は問題文の条件を満たす

# 標準入力から A, B, C の値を取得する
a, b, c = list(map(int, input().split()))

# 異なる整数を探して出力する
result = 0

if a == b:
    result = c
elif b == c:
    result = a
elif a == c:
    result = b
else:
    result = "Error"

print(result)
