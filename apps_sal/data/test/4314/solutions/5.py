n, m = map(int, input().split())
mat = []
for i in range(n):
    s = list(input())
    if '
    mat.append(s)
mat2 = []
for i in range(m):
    s = [mat[x][i] for x in range(len(mat))]
    if '
    mat2.append(s)

for i in range(len(mat2[0])):
    s = ''
    for x in range(len(mat2)):
        s += mat2[x][i]
    print(s)
