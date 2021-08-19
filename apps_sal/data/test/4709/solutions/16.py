# 050_a
A, op, B = input().split()
A = int(A)
B = int(B)
if (1 <= A & A <= 10 ** 9) & (1 <= B & B <= 10 ** 9) & ((op == '+') | (op == '-')):
    if op == '+':
        result = A + B
    elif op == '-':
        result = A - B
    print(result)
