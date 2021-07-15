def printGrid(grid):
	for row in grid:
		print(' '.join(list(map(str, row))))

n, m = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(n)]
c = 0
found = False
for i in range(1, n-1):
	if found:	break
	for j in range(1, m-1):
		if grid[i][j] == '*' and grid[i-1][j] == '*' and grid[i+1][j] == '*' and grid[i][j-1] == '*' and grid[i][j+1] == '*':
			grid[i][j] = '.'
			r, c = i-1, j
			while r >= 0:
				if grid[r][c] == '*':
					grid[r][c] = '.'
					r -= 1
				else:
					break
			r, c = i+1, j
			while r < n:
				if grid[r][c] == '*':
					grid[r][c] = '.'
					r += 1
				else:
					break
			r, c = i, j-1
			while c >= 0:
				if grid[r][c] == '*':
					grid[r][c] = '.'
					c -= 1
				else:
					break
			r, c = i, j+1
			while c < m:
				if grid[r][c] == '*':
					grid[r][c] = '.'
					c += 1
				else:
					break
			found = True
			break
if not found:
	print('NO');return
for row in grid:
	if '*' in row:
		print('NO');return
print('YES')
