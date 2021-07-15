
def mul_square_matrix(a, b, mod):
    n = len(a)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] = (ret[i][j] + a[i][k] * b[k][j]) % mod
    return ret


def power_square_matrix(mat:list, k, mod):
    n = len(mat)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    while k > 0:
        if k % 2 == 1:
            ret = mul_square_matrix(ret, mat, mod)
        mat = mul_square_matrix(mat, mat, mod)
        k //= 2
    return ret

l, a, b, m = map(int, input().split())
s_foot = a + b * (l - 1)
digit_n = len(str(s_foot))
count_digit_n = [0] * (digit_n + 1)
d = 1
for i in range(1, digit_n + 1):
    d *= 10
    x = min(d - 1, s_foot) - a
    if x < 0:
        continue
    n = x // b
    count_digit_n[i] = n + 1

for i in range(digit_n, 0, -1):
    count_digit_n[i]  -= count_digit_n[i - 1]

d = 1
x = [[0], [a], [1]]
for n in count_digit_n[1:]:
    d = d * 10 % m
    if n == 0:
        continue
    mat = [[d, 1, 0], [0, 1, b], [0, 0, 1]]
    mat = power_square_matrix(mat, n, m)
    for i in range(3):
        x[i][0] = sum([mat[i][j] * x[j][0] for j in range(3)]) % m
print(x[0][0])
