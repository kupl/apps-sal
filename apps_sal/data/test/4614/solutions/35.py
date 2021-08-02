# 入力
A, B, C = map(int, input().split())

# 処理
if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)
