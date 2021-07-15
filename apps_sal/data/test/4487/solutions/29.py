A, B, C = map(str, list(input().split())) # 文字列を一文字ずつのリスト化し複数のリストに入れる


if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")
