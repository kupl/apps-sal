from sys import stdin
_data = iter(stdin.read().split('\n'))


def input():
    return next(_data)


N = 101
MOD = 1000000007


def mul_vec_mat(v, a):
    n = len(a[0])
    m = len(v)
    c = [0] * n
    for i in range(n):
        c[i] = sum((a[j][i] * v[j] % MOD for j in range(m))) % MOD
    return c


def mul_vec_sparse_mat(v, ta):
    n = len(ta)
    c = [0] * n
    for i in range(n):
        c[i] = sum((x * v[j] % MOD for (j, x) in ta[i])) % MOD
    return c


def mod_pow_kitamasa(a, x):
    n = len(a)
    ta = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                ta[j].append((i, a[i][j]))
    r = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while x > 0:
        if x & 1:
            r[1] = mul_vec_mat(r[1], a)
        aa = [[0] * n for i in range(n)]
        aa[0] = a[0]
        aa[1] = mul_vec_mat(a[1], a)
        for i in range(2, n):
            aa[i] = mul_vec_sparse_mat(aa[i - 1], ta)
        a = aa
        x >>= 1
    for i in range(2, n):
        r[i] = mul_vec_sparse_mat(r[i - 1], ta)
    return r


(_, x) = [int(v) for v in input().split()]
a = [[0] * N for i in range(N)]
a[0][0] = 1
a[N - 1][0] = 1
for i in range(1, N - 1):
    a[i][i + 1] = 1
for d in map(int, input().split()):
    a[N - 1][N - d] += 1
a = mod_pow_kitamasa(a, x)
b = [0] * N
b[0] = 1
b[N - 1] = 1
print(sum((a[N - 1][i] * b[i] % MOD for i in range(N))) % MOD)
