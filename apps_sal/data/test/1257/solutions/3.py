(n, k) = map(int, input().split())
matrix = [[0 for i in range(n)] for j in range(n)]
cur_number = 1
for i in range(n):
    for j in range(k - 1):
        matrix[i][j] = cur_number
        cur_number += 1
for i in range(n):
    for j in range(k - 1, n):
        matrix[i][j] = cur_number
        cur_number += 1
s = 0
for i in range(n):
    s += matrix[i][k - 1]
print(s)
for i in range(n):
    print(' '.join(map(str, matrix[i])))
