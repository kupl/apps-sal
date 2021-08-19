# 数値と符号の取得
A, op, B = map(str, input().split())

# 計算して出力
calc = eval(A + op + B)
print(int(calc))
