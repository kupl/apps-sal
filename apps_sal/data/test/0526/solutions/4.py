import sys

n, m = map(int, input().split())

M = []

for i in range(n):
	M.append(list(map(int, input().split())))

result = 0
for i in range(n):
	result = result ^ M[i][0]

if result > 0:
	print('TAK')
	print(*[1 for _ in range(n)])
	return

is_solution_exist = False
row = None
col = None

for i in range(n):

	for j in range(m):

		if M[i][j] != M[i][0]:
			is_solution_exist = True
			row = i
			col = j
			break

	if is_solution_exist:
		break

if is_solution_exist:
	print('TAK')
	result = [1 for _ in range(n)]
	result[row] = col + 1
	print(*result)
else:
	print('NIE')
