import sys
input = sys.stdin.readline
n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = [0] * (3 * n)
for i in range(n):
    C[i] = B[i] ^ B[(i + 1) % n]
    C[i + n] = A[i] ^ A[(i + 1) % n]
    C[i + n + n] = C[i + n]


def z_algo(S):
    N = len(S)
    A = [0] * N
    A[0] = N
    (i, j) = (1, 0)
    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1
        A[i] = j
        if not j:
            i += 1
            continue
        k = 1
        while i + k < N and k + A[k] < j:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A


P = z_algo(C)
for (i, p) in enumerate(P[n:n + n]):
    if p >= n:
        x = A[i] ^ B[0]
        print(i, x)
