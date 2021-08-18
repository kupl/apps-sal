n, t = list(map(int, input().split()))
matrix = [[0] * i for i in range(1, n + 1)]
norma = 2**n
for time in range(t):
    matrix[0][0] += norma
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] > norma:
                many = matrix[i][j] - norma
                if i + 1 != n:
                    matrix[i + 1][j] += many // 2
                    matrix[i + 1][j + 1] += many // 2
                matrix[i][j] = norma
counter = 0
for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] == norma:
            counter += 1
print(counter)
