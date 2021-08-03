from functools import reduce


mod = 10 ** 9 + 7
M = [[0, 1, 0],
     [0, 0, 1],
     [1, 1, 1]]

E = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]


def mult(M, K):
    a, b, c = len(M), len(M[0]), len(K[0])
    # print('a, b, c:', a, b, c)
    ans = [[0 for _ in range(c)] for _ in range(a)]

    for i in range(a):
        for j in range(c):
            for k in range(b):
                ans[i][j] += (M[i][k] * K[k][j]) % (mod - 1)
                ans[i][j] %= (mod - 1)

    # 		print('ans[', i, '][', j, '] = ', ans[i][j])
    # print('mult', M, 'and', K)
    # print(ans)
    return ans


def matrix_power(M, n):
    res = E
    mtpl = M
    # print('matrix_power, n =', n)
    while n:
        if n % 2 == 1:
            res = mult(res, mtpl)
        mtpl = mult(mtpl, mtpl)
        n //= 2
    return res


n, f1, f2, f3, c = list(map(int, input().split()))
u = [c * f1 % mod, c * c * f2 % mod, c * c * c * f3 % mod]
# print('u:', u)

Mn = matrix_power(M, n - 4)
# print('Mn:', Mn)

pwrs = mult([[1, 1, 1]], Mn)
# print('pwrs:', pwrs)

arr = [pow(u[i], pwrs[0][i], mod) for i in range(3)]

un = reduce(lambda x, y: x * y % mod, arr)
# print('un:', un)

cn_1 = pow(c, n * (mod - 2) % (mod - 1), mod)
# print('cn', cn)

# cn_1 = pow(cn, mod-2, mod)
# print('cn_1', cn_1)
print((un * cn_1) % mod)
