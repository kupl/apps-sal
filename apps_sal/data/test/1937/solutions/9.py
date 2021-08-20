n = int(input())
B = list(map(int, input().split()))
A = [None] * n
A[0] = 0
A[n - 1] = B[0]
for i in range(1, n // 2):
    A[i] = max(A[i - 1], B[i] - B[i - 1] + A[i - 1])
    A[n - 1 - i] = B[i] - A[i]
for a in A:
    print(a, end=' ')
