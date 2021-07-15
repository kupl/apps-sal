n, m = list(map(int, input().split()))

A = [list(map(int, input().split())) for i in range(n)]

B = [[0 for i in range(m)] for j in range(n)]

ops = []

for i in range(n - 1):
	for j in range(m - 1):
		if all([A[i][j], A[i + 1][j], A[i][j + 1], A[i + 1][j + 1]]):
			ops.append((i + 1, j + 1))
			B[i][j] = 1
			B[i + 1][j] = 1
			B[i][j + 1] = 1
			B[i + 1][j + 1] = 1

flag = True

for i in range(n):
	for j in range(m):
		flag &= (A[i][j] == B[i][j])

if flag:
	print(len(ops))

	for o in ops:
		print(*o)
else:
	print(-1)

