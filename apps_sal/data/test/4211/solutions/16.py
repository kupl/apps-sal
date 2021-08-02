N = int(input())
B = [int(b) for b in input().split()]
A = [0] * N
A[0] = B[0]
A[1] = B[0]
for i in range(N - 1):
    if B[i] >= max(A[i], A[i]):
        A[i + 1] = B[i]
    else:
        A[i] = B[i]
        A[i + 1] = B[i]
print(sum(A))
