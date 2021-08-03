L, a, b, m = map(int, input().split())

k = 18

c = [0] * k

t = a + b * (L - 1)

p = 9
temp = 0
for i in range(k):
    if a <= p:
        c[i] = (min(p, t) - a) // b + 1 - temp
        temp += c[i]
    if t <= p:
        break
    p = (p + 1) * 10 - 1


def calc_mat(P, Q):
    ret = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ret[i][j] += P[i][k] * Q[k][j]
            ret[i][j] %= m
    return ret


s = a
x = 0
for i in range(k):
    if c[i] == 0:
        continue
    mat = [[10 ** (i + 1), 0, 0], [1, 1, 0], [0, b, 1]]
    temp_mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    d = list(reversed(bin(c[i])[2:]))
    p = 1
    for z in d:
        if z == '1':
            temp_mat = calc_mat(temp_mat, mat)
        mat = calc_mat(mat, mat)
    # print(temp_mat)
    temp_x = (temp_mat[0][0] * x + temp_mat[1][0] * s + temp_mat[2][0]) % m
    s = (temp_mat[0][1] * x + temp_mat[1][1] * s + temp_mat[2][1]) % m
    x = temp_x
    #print(x, s)

print(x)
