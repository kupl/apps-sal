(A, B, C, D) = map(int, input().split())
x = min(B, D) - max(A, C)
print(x) if x > 0 else print(0)
