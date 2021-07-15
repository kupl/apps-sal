n = int(input())

cols = []

for i in range(n):
	cols.append(list(map(int, input().split())))


left = 0
right = 0

for col in cols:
	left += col[0]
	right += col[1]

best = -1
max_raze = abs(right - left)

for i in range(n):
	_sleft = left - cols[i][0] + cols[i][1]
	_sright = right - cols[i][1] + cols[i][0]

	if abs(_sleft - _sright) > max_raze:
		best = i
		max_raze = abs(_sleft - _sright)

print(best + 1)


