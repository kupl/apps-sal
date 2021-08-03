def mat_dot(one, two, mod):
    return [[sum([(one[i][k] * two[k][j]) % mod for k in range(len(two))]) % mod for j in range(len(two[0]))] for i in range(len(one))]


def mat_pow(mat, exp, mod):
    size = len(mat)
    res = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        res[i][i] = 1
    cnt = 0
    while (1 << cnt) <= exp:
        if (exp >> cnt) & 1:
            res = mat_dot(res, mat, mod)
        mat = mat_dot(mat, mat, mod)
        cnt += 1
    return res


l, a, b, m = map(int, input().split())
c = a + (l - 1) * b
n = len(str(c))
dgt = [0 for _ in range(n + 1)]
for i in range(1, n):
    dgt[i] = max(0, (10**i - a + b - 1) // b) - max(0, (10**(i - 1) - a + b - 1) // b)
dgt[n] = l - sum(dgt)
d_sum = [0 for _ in range(n + 1)]
for i in range(n - 1, 0, -1):
    d_sum[i] = d_sum[i + 1] + dgt[i + 1] * (i + 1)
fr = [0 for _ in range(n + 1)]
fr[1] = a
for i in range(2, n + 1):
    fr[i] = fr[i - 1] + b * dgt[i - 1]
l = [[0, a % m, 1]]
for d in range(1, n + 1):
    k = [[(10**d) % m, 0, 0], [1, 1, 0], [0, b % m, 1]]
    j = mat_pow(k, dgt[d], m)
    l = mat_dot(l, j, m)

print(l[0][0] % m)
