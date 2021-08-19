M = 10 ** 9 + 7
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
(z, o) = (a.count(0), a.count(1))
d = pow(n * (n - 1) // 2, M - 2, M)
if z > o:
    (o, z) = (z, o)
    a = [1 - x for x in a][::-1]
res = [[0] * (z + 1) for i in range(z + 1)]
tf = [[0] * (z + 1) for i in range(z + 1)]
for i in range(z + 1):
    res[i][i] = 1
    tf[i][i] = (z * (z - 1) // 2 + o * (o - 1) // 2 + i * (z - i) + (z - i) * (o - z + i)) * d % M
    if i < z:
        tf[i + 1][i] = (z - i) * (z - i) * d % M
    if i:
        tf[i - 1][i] = i * (o - z + i) * d % M


def mul(a, b):
    t = [[0] * (z + 1) for i in range(z + 1)]
    for i in range(z + 1):
        for k in range(z + 1):
            for j in range(z + 1):
                t[i][j] = (t[i][j] + a[i][k] * b[k][j]) % M
    return t


while k:
    if k & 1:
        res = mul(res, tf)
    tf = mul(tf, tf)
    k >>= 1
print(res[-1][a[:z].count(0)])
