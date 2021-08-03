def mat_mult(A, B, MOD):
    n, m, p = len(A), len(A[0]), len(B[0])
    assert (len(B) == m)
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            Aik = A[i][k]
            for j in range(p):
                C[i][j] = (C[i][j] + Aik * B[k][j]) % MOD
    return C


def ksm(A, n, MOD):
    if (n == 0):
        E = [[0 for i in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            E[i][i] = 1
        return E
    if (n == 1):
        return A
    k = ksm(A, n // 2, MOD)
    z = mat_mult(k, k, MOD)
    if (n & 1):
        return (mat_mult(z, A, MOD))
    else:
        return z


def Fenjie(n):
    k = {}
    if (n == 1):
        return {}
    a = 2
    while (n >= 2):
        b = n % a
        if (a * a > n):
            k[n] = 1
            break
        if (b == 0):
            if (a in k):
                k[a] += 1
            else:
                k[a] = 1
            n = n // a
        else:
            a += 1
    return k


def Euler(n):
    if (n == 1):
        return 1
    k = Fenjie(n)
    m = n
    for i in k:
        m = m // i * (i - 1)
    return m


MOD = 10**9 + 7
n, b, c, d, e = list(map(int, input().split()))

l1 = [[0], [0], [1]]
l2 = [[0], [1], [0]]
l3 = [[1], [0], [0]]
l4 = [[6], [2], [0], [0], [0]]
a1 = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
a2 = [[3, -2, 0, -1, 1], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]]
if (n == 4):
    print(e * e * b * c * d % MOD)
else:
    a1 = ksm(a1, n - 3, MOD - 1)
    a2 = ksm(a2, n - 5, MOD - 1)
    b1 = mat_mult(a1, l1, MOD - 1)
    p1 = pow(b, b1[0][0], MOD)
    c1 = mat_mult(a1, l2, MOD - 1)
    p2 = pow(c, c1[0][0], MOD)
    d1 = mat_mult(a1, l3, MOD - 1)
    p3 = pow(d, d1[0][0], MOD)
    n1 = mat_mult(a2, l4, MOD - 1)[0][0]
    p = pow(e, n1, MOD)
    p = p1 * p % MOD
    p = p2 * p % MOD
    p = p3 * p % MOD
    print(p)
