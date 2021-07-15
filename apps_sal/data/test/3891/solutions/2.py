n, m = map(int, input().split())
arr = [input() for i in range(n)]
x_c = []
y_c = []
for i in range(n):
	for j in range(m):
		if arr[i][j] == 'B':
			x_c.append(i)
			y_c.append(j)
x_c.sort()
y_c.sort()

print(x_c[len(x_c) // 2] + 1, y_c[len(y_c) // 2] + 1)
