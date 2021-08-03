
from sys import stdin
input = stdin.buffer.readline
def I(): return list(map(int, input().split()))


mat = []
for _ in range(int(input())):
    mat.append(I())
n = len(mat)


def sumDiag(mat):
    diag_sum = []
    diag_sum2 = []
    n = len(mat)
    for i in range(n):
        s = 0
        for j in range(0, n - i):
            s += mat[j][(j + i)]
        diag_sum.append(s)
        if i != 0:
            s = 0
            for j in range(0, n - i):
                s += mat[j + i][(j)]
            diag_sum2.append(s)
    return diag_sum2[::-1] + diag_sum


def antiDiag(mat):
    def mirror(mat):
        for i in range(len(mat)):
            for j in range(len(mat[0]) // 2):
                t = mat[i][j]
                mat[i][j] = mat[i][len(mat[0]) - 1 - j]
                mat[i][len(mat[0]) - 1 - j] = t
        return mat
    mat = mirror(mat)
    out = sumDiag(mat)
    mirror(mat)
    return out[::-1]


d1 = sumDiag(mat)
d2 = antiDiag(mat)


def ret(i, j):
    return d1[n - 1 - (i - j)] + d2[i + j] - mat[i][j]


m1 = 0
m2 = 0
best1 = (1, 1)
best2 = (1, 2)
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0 and m1 < ret(i, j):
            m1 = ret(i, j)
            best1 = (i + 1, j + 1)
        elif (i + j) % 2 == 1 and m2 < ret(i, j):
            m2 = ret(i, j)
            best2 = (i + 1, j + 1)

print(m1 + m2)
print(" ".join(map(str, [best1[0], best1[1], best2[0], best2[1]])))
