N = int(input())
B = list(map(int, input().split()))
A = [0] * N
(A[0], A[N - 1]) = (B[0], B[N - 2])
for i in range(1, N - 1):
    A[i] = min(B[i - 1], B[i])
print(sum(A))
