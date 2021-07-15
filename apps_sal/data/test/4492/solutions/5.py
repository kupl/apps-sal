import sys

N, X = map(int, input().split())
A = list(map(int, sys.stdin.readline().rsplit()))
B = A[::]

for i in range(N - 1):
    a = A[i] + A[i + 1]
    if a > X:
        if A[i + 1] >= a - X:
            A[i + 1] -= a - X
        else:
            A[i] -= a - X - A[i + 1]
            A[i + 1] = 0

res = 0
for i in range(N):
    res += B[i] - A[i]

print(res)
