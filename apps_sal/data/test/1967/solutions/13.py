a, b = [int(i) for i in input().split()]


matrix_in = [[0 for i in range(a)] for j in range(b)]
for i in range(b):
    line = input()
    for j in range(a):
        matrix_in[i][j] = line[j]

# Right rotate and flip
matrix_rotated = [[0 for i in range(b)] for j in range(a)]
for i in range(a):
    for j in range(b):
        matrix_rotated[i][j] = matrix_in[j][i]

# Print
for i in range(a):
    toprint=""
    for j in range(b): 
        toprint += matrix_rotated[i][j]*2
    print(toprint)
    print(toprint)

