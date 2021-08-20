(A, B, C, D) = list(map(int, input().split()))
print(max(max(A, B) * max(C, D), min(A, B) * max(C, D), max(A, B) * min(C, D), min(A, B) * min(C, D)))
