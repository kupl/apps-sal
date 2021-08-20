def unitmat(n):
    return [[int(i == j) for i in range(n)] for j in range(n)]


def matadd(A, B):
    h = len(A)
    w = len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(w)] for i in range(h)]
    return C


def matmul(A, B):
    h = len(A)
    w = len(B[0])
    l = len(B)
    C = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(l):
                C[i][j] += A[i][k] * B[k][j]
    for i in range(h):
        for j in range(w):
            C[i][j] %= mod
    return C


def matpow(A, k):
    n = len(A)
    B = unitmat(n)
    while k:
        if k & 1:
            B = matmul(B, A)
        A = matmul(A, A)
        k >>= 1
    return B


(l, a, b, mod) = map(int, input().split())
X = [[0], [a], [1]]
maxdigit = 18
Idx = [0] * (maxdigit + 1)
for i in range(maxdigit + 1):
    if 10 ** i - 1 < a:
        continue
    Idx[i] = min((10 ** i - 1 - a) // b + 1, l)
for i in range(1, maxdigit + 1):
    f = [[10 ** i, 1, 0], [0, 1, b], [0, 0, 1]]
    X = matmul(matpow(f, Idx[i] - Idx[i - 1]), X)
print(X[0][0])
