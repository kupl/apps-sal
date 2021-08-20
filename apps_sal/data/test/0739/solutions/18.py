def mpw(n, m):
    ret = 1
    while m > 0:
        if m & 1:
            ret *= n
            ret %= M
        n *= n
        n %= M
        m >>= 1
    return ret


def pw(n, m):
    ret = 1
    while m > 0:
        if m & 1:
            ret *= n
        n *= n
        m >>= 1
    return ret


def delta(i, j):
    if i == j:
        return 1
    return 0


def mtxmpw(A, m):
    ret = [[delta(i, j) for i in range(len(A))] for j in range(len(A))]
    while m > 0:
        if m & 1:
            ret = mul(ret, A)
        A = mul(A, A)
        m >>= 1
    return ret


def mul(A, B):
    ret = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ret[i][j] += A[i][k] * B[k][j]
                ret[i][j] %= M
    return ret


(L, A, B, M) = map(int, input().split())
ans = 0
d = 0
for k in range(18, 0, -1):
    l = max((pw(10, k - 1) - A + B - 1) // B, 0)
    r = min((pw(10, k) - A - 1) // B, L - 1)
    if l <= r:
        MT = [[1, mpw(10, k), 0], [0, mpw(10, k), (M - B * mpw(10, k) % M) % M], [0, 0, mpw(10, k)]]
        v = [[(A + B * r) % M], [(A + B * (r - 1) % M + M) % M], [1]]
        u = mul(mtxmpw(MT, r - l), v)
        ans += mpw(10, d) * u[0][0] % M
        ans %= M
        d += (r - l + 1) * k
print(ans)
