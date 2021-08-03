# 入力
A, op, B = map(str, input().split())

# 処理
A = int(A)
B = int(B)
if op == '+':
    print(A + B)
else:
    print(A - B)
