# 3 つの整数 A , B , C が与えられます。 A , B , C のうち 2 つは 同じ整数であり、残りの 1 つだけ異なる整数です。
# 例えば、 A = 5 , B = 7 , C = 5 の場合、 A , C の 2 つは同じ整数であり、 B は 1 つだけ異なる整数です。
# 3 つの整数のうち、 1 つだけ異なる整数を求めてください。

A, B, C = map(int, input().split())

if A == B:
    print(C)

elif A == C:
    print(B)

elif B == C:
    print(A)
