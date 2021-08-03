def mmult(A, B):
    nonlocal mod
    n, m, l = len(A), len(B), len(B[0])
    ret = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                ret[i][k] = (ret[i][k] + A[i][j] * B[j][k]) % mod
    return ret


def mpow(A, n):
    if n == 0:
        return [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    if n % 2:
        return mmult(mpow(A, n - 1), A)
    return mpow(mmult(A, A), n // 2)


L, A, B, mod = map(int, input().split())
Y = [max((10**i - A + B - 1) // B, 0) for i in range(20)]
s = 0
for i in range(19):
    a, b, n = A + B * Y[i], B, max(min(L, Y[i + 1]) - Y[i], 0)
    M = [[10**(i + 1), 0, 0], [1, 1, 0], [0, 1, 1]]
    s = mmult([[s, a, b]], mpow(M, n))[0][0]

print(s)
