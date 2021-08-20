N = int(input())
A = list(map(int, input().split()))
result = 0
for i in range(1, N):
    if A[i] < A[i - 1]:
        result += A[i - 1] - A[i]
        A[i] = A[i - 1]
print(result)
