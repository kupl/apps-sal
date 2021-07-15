x = int(input())
k = [1, 2]
w = 0
for i in range(x):
	n = int(input())
	if k.count(n) == 0:
		w = 1
		break
	k[1 - k.index(n)] = 6 - k[0] - k[1]
if w == 1:
	print('NO')
else:
	print('YES')

