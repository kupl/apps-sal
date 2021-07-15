n, m = map(int, input().split())
mat1 = [[0 for i in range(m)] for j in range(n)]
mat2 = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    mat1[i] = list(map(int, input().split()))
for i in range(n):
    mat2[i] = list(map(int, input().split()))
l1 = [dict() for i in range(n + m - 1)]
l2 = [dict() for i in range(n + m - 1)]
for i in range(n):
    for j in range(m):
        if mat1[i][j] in l1[i + j]:
            l1[i + j][mat1[i][j]] += 1
        else:
            l1[i + j][mat1[i][j]] = 1
        if mat2[i][j] in l2[i + j]:
            l2[i + j][mat2[i][j]] += 1
        else:
            l2[i + j][mat2[i][j]] = 1
flag = 0
for i in range(n + m - 1):
    if l1[i] != l2[i]:
        flag = 1
print(flag * "NO" + (1 - flag) * "YES")
