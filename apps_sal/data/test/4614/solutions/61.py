# A - One out of Three

# 入力された整数A,B,Cのうち、2つは等しく1つは異なる
# 1つだけ異なる整数の値を出力する


A, B, C = list(map(int, input().split()))

if A == B:
    print(C)
elif A == C:
    print(B)
elif B == C:
    print(A)
