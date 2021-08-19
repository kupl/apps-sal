# 入力
A, op, B = input().split()
A, B = int(A), int(B)

# 処理
if op == '+':
    S = A + B
else:
    S = A - B
# 出力
print(S)
