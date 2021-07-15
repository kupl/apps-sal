n, m = map(int, input().split())

array = []
row_sums = [0 for x in range(n)]

for i in range(n):
	array.append(list(map(int, input().split())))
	row_sums[i] = sum(array[i])

col_sums = [sum(x) for x in zip(*array)]

min_row_index = row_sums.index(min(row_sums))
min_col_index = col_sums.index(min(col_sums))


row_boost = [0 for x in range(n)]
col_boost = [0 for x in range(m)]
#rows contribute more
if n <= m:
	#get largest row add possible
	col_boost[min_col_index] = 0
	for i in range(m):
		if i != min_col_index:
			col_boost[i] = (col_sums[i] - col_sums[min_col_index]) // n

		sum_col_boosts = sum(col_boost)

		for i in range(n):
			row_boost[i] = (row_sums[i] - sum_col_boosts) // m

if n >= m:
	row_boost[min_row_index] = 0

	for i in range(n):
		if i != min_row_index:
			row_boost[i] = (row_sums[i] - row_sums[min_row_index]) // m

	sum_row_boosts = sum(row_boost)

	for i in range(m):
		col_boost[i] = (col_sums[i] - sum_row_boosts) // n

for row in range(n):
	if [row_boost[row] + c for c in col_boost] != array[row]:
		print(-1)
		return

print(sum(row_boost + col_boost))
for i in range(n):
	for count in range(row_boost[i]):
		print('row ' + str(i+1))

for j in range(m):
	for count in range(col_boost[j]):
		print('col ' + str(j+1))
