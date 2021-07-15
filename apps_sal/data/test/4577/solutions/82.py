# A - Between Two Integers

# 整数A,B,Cが入力される
# CがA以上かつB以下であるかを判定する


A,B,C = list(map(int,input().split()))

if A<=C and B>=C:
    print('Yes')
else:
    print('No')

