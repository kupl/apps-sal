inin = input().split(' ')
n = int(inin[0])
t = int(inin[1])
mat = []
for i in range(n + 2):
    mat.append([0.0] * (n + 2))
for time in range(t):
    mat[1][1] += 1.0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if mat[i][j] > 1.0:
                over = mat[i][j] - 1.0
                mat[i + 1][j] += over / 2
                mat[i + 1][j + 1] += over / 2
                mat[i][j] = 1.0
result = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if mat[i][j] >= 1.0:
            result += 1
print(result)
