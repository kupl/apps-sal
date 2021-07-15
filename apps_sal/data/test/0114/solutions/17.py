n, m = list(map(int, input().split()))
l = []
for i in range(n):
	l.append(list(map(int, input().split())))
b = [[0] * m for _ in range(n)]
ops = []
for i in range(n - 1):
	for j in range(m - 1):
		if l[i][j] == 1 and l[i + 1][j] == 1 and l[i][j + 1] == 1 and l[i + 1][j + 1] == 1:
			ops.append([i + 1, j + 1])
			for x in range(2):
				for y in range(2):
					b[i + x][j + y] = 1
if l == b:
	print(len(ops))
	for i in ops:
		print(i[0], i[1])
else:
	print(-1)

