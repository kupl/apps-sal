N, M = map(int, input().split())
H = list(map(int, input().split()))
A = list(range(1, N + 1))
for i in range(M):
    a, b = map(int, input().split())
    if H[a - 1] > H[b - 1]:
        A[b - 1] = 0
    elif H[a - 1] < H[b - 1]:
        A[a - 1] = 0
    else:
        A[a - 1] = 0
        A[b - 1] = 0
print(N - A.count(0))
