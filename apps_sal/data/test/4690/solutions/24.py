(A, B, C, D) = map(int, input().split())
print(A * B if A * B == C * D else max(A * B, C * D))
