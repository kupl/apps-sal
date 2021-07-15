a = []
for i in range(4):
	a += [input()]
f = False
for i in range(4):
	for j in range(2):
		f |= a[i][j: j + 3].count('.') == 1 and a[i][j: j + 3].count('o') == 0
for j in range(4):
	for i in range(2):
		f |= ([a[i][j]] + [a[i + 1][j]] + [a[i + 2][j]]).count('.') == 1 and ([a[i][j]] + [a[i + 1][j]] + [a[i + 2][j]]).count('o') == 0
for i in range(2):
	for j in range(2):
		f |= [a[i][j], a[i + 1][j + 1], a[i + 2][j + 2]].count('.') == 1 and [a[i][j], a[i + 1][j + 1], a[i + 2][j + 2]].count('o') == 0
		f |= [a[3 - i][j], a[2 - i][j + 1], a[1 - i][j + 2]].count('.') == 1 and [a[3 - i][j], a[2 - i][j + 1], a[1 - i][j + 2]].count('o') == 0
if f:
	print('YES')
else:
	print('NO')
