n, a, b, MOD = list(map(int, input().split()))


def matmul(A, B):
    nonlocal MOD
    N, M, L = len(A), len(B), len(B[0])
    ret = [[0 for j in range(L)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(L):
                ret[i][k] += A[i][j] * B[j][k] % MOD
                ret[i][k] %= MOD
    return ret


ans, c = [[0, a % MOD, 1]], 0
for i in range(1, 19):
    if not a < 10**i:
        continue
    m = [[10**i % MOD, 0, 0], [1, 1, 0], [0, b % MOD, 1]]
    q = -c
    c = min(((10**i - 1 - a) // b) + 1, n)
    q += c
    while q:
        if q & 1:
            ans = matmul(ans, m)
        m = matmul(m, m)
        q >>= 1
print((ans[0][0]))
