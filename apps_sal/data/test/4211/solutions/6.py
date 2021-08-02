N = int(input())
B = list(map(int, input().split()))
A = [0] * N
for i in range(N):
    A[i] = B[i - 1]
    if A[i - 1] > B[i - 1]:
        A[i - 1] = B[i - 1]
A[0] = B[0]
print(sum(A))
