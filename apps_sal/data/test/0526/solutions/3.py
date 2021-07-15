def groupxor(l):
	result = 0
	for item in l:
		result = result ^ item
	return result

r,c = [int(x) for x in input().split()]
rows = []
for _ in range(r):
	rows.append([int(x) for x in input().split()])
starts = [rows[j][0] for j in range(r)]
result = [1] * r
if groupxor(starts) == 0:
	notfixed = True
	for j in range(r):
		for k in range(1,c):
			if notfixed:
				if rows[j][0] != rows[j][k]:
					notfixed = False
					result[j] = k+1
	if notfixed == True:
		print('NIE')
	else:
		print('TAK')
		print(' '.join([str(x) for x in result]))
else:
	print('TAK')
	print(' '.join([str(x) for x in result]))
