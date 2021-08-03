n = int(input())
A = list(map(int, input().split()))
X = [0] * n
S = sum(A)
A2 = 0
for i in range(1, n - 1, 2):
    A2 += A[i]
X[0] = S - 2 * A2
for i in range(1, n):
    X[i] = 2 * A[i - 1] - X[i - 1]
print(*X)
