n, k = map(int, input().split())

mat = [[0] * n for i in range(n)]

for i in range(n):
    mat[i][i] = k
for x in mat:
    print(*x)
