def is_available(i, j):
    return i < n and j < n and (matrix[i][j] == 0)


(n, k) = list(map(int, input().split()))
if k > n * n:
    print(-1)
else:
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    if k % 2 == 1:
        matrix[0][0] = 1
        k -= 1
    for i in range(n):
        for j in range(n):
            if k == 0:
                i = n
                break
            if matrix[i][j] == 1:
                continue
            if i == j:
                matrix[i + 1][j + 1] = matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[j][i] = 1
            k -= 2
    print('\n'.join([' '.join(map(str, row)) for row in matrix]))
