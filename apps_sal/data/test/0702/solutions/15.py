n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
for i in range(n-2):
    for j in range(1, n-1):
        if matrix[i][j]=='.':
            if matrix[i+1][j]=='.' and matrix[i+2][j]=='.' and matrix[i+1][j-1]=='.' and matrix[i+1][j+1]=='.':
                matrix[i][j]='#'; matrix[i+1][j]='#'; matrix[i+2][j]='#'; matrix[i+1][j-1]='#'; matrix[i+1][j+1]='#'
            else: print('NO'); return
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='.': print('NO'); return
print('YES')

