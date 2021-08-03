l, a, b, mod = map(int, input().split())


def mul(m1, m2):
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            m[i][j] = sum(m1[i][k] * m2[k][j] for k in range(3)) % mod
    return m

# mat = [[1, 0, 0],
#        [0, 1, 0],
#        [0, 0, 1]]
# vec = (0, a, 1)


mat = [[0, 0, 0],
       [a, 0, 0],
       [1, 0, 0]]
d = 1
e = a + b * (l - 1)
while e >= d:
    d *= 10
    if a >= d:
        continue
    t = (min(d - 1, e) - a) // b + 1
    a += b * t
    bit = [[d, 1, 0],
           [0, 1, b],
           [0, 0, 1]]
    while t > 0:
        if t & 1:
            mat = mul(bit, mat)
        bit = mul(bit, bit)
        t //= 2

# print((mat[0][0] * vec[0] + mat[0][1] * vec[1] + mat[0][2] * vec[2]) % mod)
print(mat[0][0])
