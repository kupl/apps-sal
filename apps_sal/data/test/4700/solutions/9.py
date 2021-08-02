N, M = map(int, input().split())
H = list(map(int, input().split()))
A, B = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

L = [1] * N

for i in range(M):
    ai = A[i] - 1
    bi = B[i] - 1
    if H[ai] > H[bi]:
        L[bi] = 0
    elif H[bi] > H[ai]:
        L[ai] = 0
    else:
        L[ai], L[bi] = 0, 0

print(L.count(1))
