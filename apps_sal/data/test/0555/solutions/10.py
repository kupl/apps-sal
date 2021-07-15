x = list(map(int, input()))
if len(x) == 1:
	x = x[0]
	if x <= 4:
		print(x)
	elif x <= 8:
		print(9 - x)
	elif x == 9:
		print(9)
	return
if 5 <= x[0] <= 8:
	x[0] = 9 - x[0]
for i in range(1, len(x)):
	if x[i] >= 5:
		x[i] = 9 - x[i]
print(''.join(map(str, x)))


