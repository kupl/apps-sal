# 二つの整数 A , B が入力されます。 A + B の値を出力してください。
# ただし、 A + B が 10 以上の場合は、代わりに error と出力してください。

A, B = map(int, input().split())

if A + B <= 9:
    print(A + B)

else:
    print('error')
