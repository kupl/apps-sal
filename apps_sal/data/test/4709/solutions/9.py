# A op Bという式の値を計算

A, op, B = map(str, input().split())
A = int(A)
B = int(B)

if op == '+':
    print(A + B)
else:
    print(A - B)
