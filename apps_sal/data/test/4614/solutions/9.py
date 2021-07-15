# 3つの整数のうち1つだけ異なる値を出力
A, B, C = map(int,input().split())

if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)
