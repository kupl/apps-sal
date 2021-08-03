N = int(input())
B = list(map(int, input().split()))

A = [0] * N
A[0] = B[0]

for i in range(1, N - 1):
    A[i] = min(B[i], B[i - 1])

A[N - 1] = B[N - 2]

print((sum(A)))
