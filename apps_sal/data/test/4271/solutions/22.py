N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = 0
for i in range(N):
    s += B[A[i] - 1]
    if i < N - 1:
        if A[i] + 1 == A[i + 1]:
            s += C[A[i] - 1]

print(s)
