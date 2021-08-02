A, B, _, K = map(int, input().split())
print(B - K + A * 2if A + B < K else min(A, K))
