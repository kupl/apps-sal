t = int(input())
for _ in range(t):
	n, m = list(map(int, input().split()))
	mat = []
	for i in range(n):
		mat += [[int(j) for j in input().split()]]


	for i in range(n):
		for j in range(m):
			if (i+j)%2 == 0:
				if mat[i][j]%2 == 1:
					mat[i][j] += 1
			else:
				if mat[i][j]%2 == 0:
					mat[i][j] += 1

	for x in mat:
		print(*x)

