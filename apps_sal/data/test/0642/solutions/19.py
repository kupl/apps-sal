n, m = [int(x) for x in input().split()]
if m:
	l = sorted([int(x) for x in input().split()])
else:
	l = []
if len(l) and (l[0] == 1 or l[-1] == n):
	print('NO')
	return
for i in range(m - 2):
	if l[i + 2] == l[i + 1] + 1 and l[i + 1] == l[i] + 1:
		print('NO')
		break
else:
	print('YES')

