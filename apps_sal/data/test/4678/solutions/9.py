N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N - 1):
    if A[i] > A[i + 1]:
        count += A[i] - A[i + 1]
        A[i + 1] = A[i]
print(count)
