import math
md = 10**9 + 7


def multiply(M, N):
    md2 = 10**9 + 6
    R = [[0 for i in range(3)] for j in range(3)]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                R[i][j] += (M[i][k] * N[k][j]) % md2
                R[i][j] %= md2
    return R


def power(mat, n):
    res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while n:
        if n & 1: res = multiply(res, mat)
        mat = multiply(mat, mat)
        n //= 2
    return res


n, f1, f2, f3, c = map(int, input().split())
f1 = (f1 * c) % md
f2 = (f2 * c**2) % md
f3 = (f3 * c**3) % md
#print(f1, f2, f3)
mat = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
res = power(mat, n - 3)
# print(res)
pw1, pw2, pw3 = res[0][2], res[0][1], res[0][0]
f1 = pow(f1, pw1, md)
f2 = pow(f2, pw2, md)
f3 = pow(f3, pw3, md)
ans = ((f1 * f2) % md * f3) % md
c = pow(c, md - 2, md)
ans *= pow(c, n % (md - 1), md)
ans %= md
print(ans)
