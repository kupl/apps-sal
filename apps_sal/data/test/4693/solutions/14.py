# 二つの整数A,Bの和 10以上ならerrorと出力

A, B = map(int, input().split())

if A + B < 10:
    print(A + B)
else:
    print('error')
