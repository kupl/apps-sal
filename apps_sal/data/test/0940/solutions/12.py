A = list(map(int, input().split()))
A = sorted(A)
print(max(0, A[2] - A[0] - A[1] + 1))
