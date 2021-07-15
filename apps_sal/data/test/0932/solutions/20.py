a, b = list(map(int, input().split(' ')))
array = [[1] * b for i in range(a)]
orig = [list(map(int, input().split(' '))) for i in range(a)]
matrix = []
for i in orig:
    matrix.append(i[:])

row0 = []
col0 = []
for i in range(a):
    for j in range(b):
        if matrix[i][j] == 0:
            row0.append(i)
            col0.append(j)
            
row0 = list(set(row0))
col0 = list(set(col0))
for i in row0:
    matrix[i] = [0] * b
for ele in col0:
    for i in range(a):
        matrix[i][ele] = 0

match = [[0] * b for i in range(a)]
for i in range(len(matrix)):
    if 1 in matrix[i]:
        match[i] = [1] * len(matrix[0])

jlist = []
for i in range(a):
    for j in range(b):
        if matrix[i][j] == 1:
            jlist.append(j)
for i in jlist:
    for bad in range(len(match)):
        match[bad][i] = 1
if match == orig:
    print("YES")
    for i in matrix:
        print(' '.join([str(j) for j in i]))

else:
    print("NO")

