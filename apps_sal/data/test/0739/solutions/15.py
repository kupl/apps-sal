l, a, b, MOD = [int(item) for item in input().split()]
vec = [0, a%MOD, 1]

def mat_mat_mul3(m1, m2):
    m3 = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                m3[i][j] += m1[i][k] * m2[k][j]
                m3[i][j] %= MOD
    return m3

def mat_vec_mul3(m1, v1):
    v2 = [0] * 3
    for i in range(3):
        for k in range(3):
            v2[i] += v1[k] * m1[i][k]
            v2[i] %= MOD
    return v2

A_d_pow = [[None] * 66 for _ in range(20)]
for d in range(20):
    for i in range(66):
        if i == 0:
            A = [[1, 0, 0], 
                 [0, 1, 0], 
                 [0, 0, 1]]
            A_d_pow[d][i] = A
            continue
        if i == 1:
            A = [[10**d % MOD, 1, 0], 
                 [0, 1, b % MOD], 
                 [0, 0, 1]]
            A_d_pow[d][i] = A
            continue
        A_d_pow[d][i] = mat_mat_mul3(A_d_pow[d][i-1], A_d_pow[d][i-1])

multimes = [0] * 20
for i in range(1,20):
    if 10**i > a:
        cnt = (10**i - 1 - a) // b + 1
        if cnt >= l:
            multimes[i] = l
            break
        else:
            multimes[i] = cnt
            l -= cnt
            a += cnt * b

for i, num in enumerate(multimes):
    if num == 0:
        continue
    for j in range(66):
        if num & 1 << j:
            vec = mat_vec_mul3(A_d_pow[i][j+1], vec)

print(vec[0])
