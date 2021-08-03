N = int(input())
B = list(map(int, input().split()))
A = list([0] * N)
for i in range(N - 2):
    A[i + 1] = min(B[i], B[i + 1])
A[0] = B[0]
A[N - 1] = B[N - 2]
print(sum(A))
