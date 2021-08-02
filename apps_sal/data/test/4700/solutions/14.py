N, M = map(int, input().split())
H = list(map(int, input().split()))
A = [0] * M
B = [0] * M
C = [0] * N
for i in range(M):
    A[i], B[i] = map(int, input().split())

for i in range(M):
    if H[A[i] - 1] < H[B[i] - 1]:
        C[A[i] - 1] += 1
    elif H[A[i] - 1] > H[B[i] - 1]:
        C[B[i] - 1] += 1
    else:
        C[A[i] - 1] += 1
        C[B[i] - 1] += 1
print(C.count(0))
