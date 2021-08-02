from math import sqrt
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

a0 = int(sqrt(matrix[0][1] * matrix[0][2] / matrix[1][2]))
print(a0, end=' ')
for i in range(1, n):
    print(int(matrix[0][i] / a0), end=' ')

print('')
