# 3つの整数A,B,C。CがA以上かつB以下か判定。

A, B, C = map(int, input().split())

if A <= C <= B:
    print('Yes')
else:
    print('No')
