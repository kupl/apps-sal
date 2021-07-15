# A - Addition and Subtraction Easy

# A, op, B の入力を受け取り、演算結果を出力する


A, op, B = input().split()

if op == '+':
    print((int(A) + int(B)))
elif op == '-':
    print((int(A) - int(B)))

