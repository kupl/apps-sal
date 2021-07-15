n = int(input())
matrix = [[1 for i in range(n)] for j in range(n)]
for y in range(1, n):
	for x in range(1, n):
		matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]
print(matrix[n - 1][n - 1])

