# 入力
A, B, C = map(int, input().split())

# CがA以上かつB以下ならYes、違うならNo
if A <= C <= B:
    print('Yes')
else:
    print('No')
