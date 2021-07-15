n, m, q = map(int, input().split())
queries = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(q)]
matrix = [[0]*m for i in range(n)]
while queries:
    query = queries.pop()
    if query[0] == 0:
        row = [matrix[query[1]][-1]]
        row.extend(matrix[query[1]][:-1])
        matrix[query[1]] = row
    elif query[0] == 1:
        cell = matrix[n-1][query[1]]
        for i in range(n):
            matrix[i][query[1]], cell = cell, matrix[i][query[1]]
    else:
        matrix[query[1]][query[2]] = query[3] + 1
[print(*row) for row in matrix]

