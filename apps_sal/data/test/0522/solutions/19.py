def mat_pow(mat, count):
    res = mat
    for x in map(int, bin(count)[3:]):
        res = mat_mat_mul(res, res)
        if x:
            res = mat_mat_mul(res, mat)
    return res
    
def mat_mat_mul(mat1, mat2):
    nonlocal mod
    d = len(mat1)
    res = []
    for row in range(d):
        res.append([])
        for col in range(d):
            cur = 0
            for i in range(d):
                cur += mat1[row][i] * mat2[i][col]
                cur %= mod - 1
            res[-1].append(cur)
    return res
    
def mat_vec_mul(mat, vec):
    nonlocal mod
    res = []
    for row in mat:
        cur = 0
        for r, c in zip(row, vec):
            cur += r * c
            cur %= mod - 1
        res.append(cur)
    return res

mod = 10**9 + 7

n, x1, x2, x3, c = list(map(int, input().split()))

# [n-2, n-1, n]
x1_init = [1, 0, 0]
x1_mat = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

# [n-2, n-1, n]
x2_init = [0, 1, 0]
x2_mat = x1_mat

# [n-2, n-1, n]
x3_init = [0, 0, 1]
x3_mat = x1_mat

# [count_n-2, count_n-1, count_n, n, 1]
c_init = [0, 0, 0, 3, 1]
c_mat = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 2, -4],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]

x1_count = mat_vec_mul(mat_pow(x1_mat, n-1), x1_init)[0]
x2_count = mat_vec_mul(mat_pow(x2_mat, n-1), x2_init)[0]
x3_count = mat_vec_mul(mat_pow(x3_mat, n-1), x3_init)[0]
c_count = mat_vec_mul(mat_pow(c_mat, n-1), c_init)[0]

ans = pow(c, c_count, mod) * pow(x1, x1_count, mod) * pow(x2, x2_count, mod) * pow(x3, x3_count, mod)
ans %= mod
print(ans)

