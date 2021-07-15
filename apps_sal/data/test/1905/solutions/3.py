a, b, c = map(int, input().split())
arr = []
mat = [[0 for j in range(b)] for i in range(a)]
for i in range(c):
    arr.append(input())
arr = arr[::-1]
for command in arr:
    arra = [int(i) for i in command.split()]
    if arra[0] == 1:
        swp = mat[arra[1] - 1][b - 1]
        for i in range(b):
            mat[arra[1] - 1][i], swp = swp, mat[arra[1] - 1][i]
    elif arra[0] == 2:
        swp = mat[a - 1][arra[1] - 1]
        for i in range(a):
            mat[i][arra[1] - 1], swp = swp, mat[i][arra[1] - 1]
    else:
        mat[arra[1] - 1][arra[2] - 1] = arra[3]
for i in mat:
    for j in i:
        print(j, end=" ")
    print()
