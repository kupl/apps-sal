# 入力
A, B, C = map(int, input().split())

# 比較して出力
if A == B:
    print(C)
elif A == C:
    print(B)
elif B == C:
    print(A)
