N = int(input())
A = [int(input()) for _ in range(N)]
M1 = max(A[0], A[1])
M2 = min(A[0], A[1])
for i in range(2, N):
    if A[i] >= M1:
        M2 = M1
        M1 = A[i]
    else:
        M2 = max(M2, A[i])
for i in range(N):
    if A[i] == M1:
        print(M2)
    else:
        print(M1)
