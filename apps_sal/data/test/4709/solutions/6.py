# 入力
A, op, B = list(map(str, input().split()))

# +なら足す、-なら引く
if op == '+':
    print((int(A) + int(B)))
elif op == '-':
    print((int(A) - int(B)))

