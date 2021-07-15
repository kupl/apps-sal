A = list(map(int, input().split()))
A, d = sorted(A[:3]), A[3]
print(max(0, d - A[1] + A[0]) + max(0, d - A[2] + A[1]))

