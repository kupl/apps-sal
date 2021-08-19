N = int(input())
A = list(map(int, input().split()))
X = [0] * N
S = 0
As = 0
for i in range(N):
    S += A[i]
for i in range((N - 1) // 2):
    As += A[2 * i + 1]
X[0] = S - 2 * As
for i in range(1, N):
    X[i] = 2 * A[i - 1] - X[i - 1]
s = ''
for i in range(N):
    s += str(X[i]) + ' '
print(s)
