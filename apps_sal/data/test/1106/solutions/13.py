n = int(input())
A = [0] + list(map(int, input().split()))
C = 0
for i in range(2 ** n - 2, -1, -1):
    C += abs(A[i * 2 + 1] - A[i * 2 + 2])
    A[i] += max(A[i * 2 + 1], A[i * 2 + 2])
print(C)
