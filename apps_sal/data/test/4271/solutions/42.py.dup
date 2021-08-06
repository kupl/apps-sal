N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

S = 0
for i in range(N - 1):
    if A[i + 1] == A[i] + 1:
        S += B[A[i] - 1] + C[A[i] - 1]
    else:
        S += B[A[i] - 1]

S += B[A[N - 1] - 1]
print(S)
