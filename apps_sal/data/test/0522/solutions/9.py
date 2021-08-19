def mat_dot(A, B, mod):
    assert len(A[0]) == len(B), 'invalid_size'

    L = len(A)
    M = len(A[0])
    N = len(B[0])

    res = [[0] * N for _ in range(L)]

    for i in range(L):
        for j in range(N):
            a = 0
            for k in range(M):
                a = (a + A[i][k] * B[k][j]) % mod
            res[i][j] = a

    return res


def mat_pow(A, x, mod):
    N = len(A)
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if 2**i & x:
            res = mat_dot(res, A, mod)
        A = mat_dot(A, A, mod)
    return res

# if there exists K such that X**K %mod == Y % mod, return K % (mod-1)
# Otherwise, return -1


def bsgs(X, Y, mod):
    Y %= mod
    X %= mod

    rm = int(mod**(0.5)) + 2
    R = pow(pow(X, rm, mod), mod - 2, mod)

    D = {Y: 0}
    p = Y
    for a in range(1, rm):
        p = p * R % mod
        D[p] = a

    p = 1
    b = 0
    if p in D:
        return (D[p] * rm + b) % (mod - 1)
    for b in range(1, rm):
        p = (p * X) % mod
        if p in D:
            return (D[p] * rm + b) % (mod - 1)
    return -1


n, f1, f2, f3, c = list(map(int, input().split()))
mod = 10**9 + 7
a1 = bsgs(5, f1, mod)
a2 = bsgs(5, f2, mod)
a3 = bsgs(5, f3, mod)
d = bsgs(5, c, mod)
A = [[1, 1, 1, 2 * d, -6 * d],
     [1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 0, 1]]
B = mat_pow(A, n - 3, mod - 1)
Ans = mat_dot(B, [[a3], [a2], [a1], [4], [1]], mod - 1)
print(pow(5, Ans[0][0], mod))
