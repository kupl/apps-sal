with open(0) as f:
    C = [list(map(int, line.split())) for line in f.readlines()]
b = [(C[i][1]-C[i][0], C[i][2]-C[i][1]) for i in range(3)]
a = [(C[1][j]-C[0][j], C[2][j]-C[1][j]) for j in range(3)]
print('Yes' if a[0]==a[1]==a[2] and b[0]==b[1]==b[2] else 'No')
