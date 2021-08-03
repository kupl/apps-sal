N = int(input())
B = [int(n) for n in input().split()]

A = [0] * N

A[0] = B[0]
A[-1] = B[-1]

for i in range(1, N - 1):
    A[i] = B[i - 1]

    if A[i] > B[i]:
        A[i] = B[i]

print(sum(A))
