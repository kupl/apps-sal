rt, ct = map(int, input().split())
grid = [[-1 for x in range(ct)] for y in range(rt)]

rows = list(map(int, input().split()))
cols = list(map(int, input().split()))

can = True
for r in range(len(rows)):
	rc = rows[r];
	for i in range(rc):
		if(grid[r][i] == 0):
			can = False
			break
		grid[r][i] = 1
	if (rc < ct):
		if (grid[r][rc] == 1):
			can = False
			break
		grid[r][rc] = 0
	
for c in range(len(cols)):
	if(not can):
		break
	cc = cols[c];
	for i in range(cc):
		if(grid[i][c] == 0):
			can = False
			break
		grid[i][c] = 1
	if (cc < rt):
		if(grid[cc][c] == 1):
			can = False
			break
		grid[cc][c] = 0

if(not can):
	print(0)
else:
	cnt = 0
	for i in range(len(grid)):
		row = grid[i]
		for j in row:
			if (j == -1):
				cnt += 1
	print(pow(2,cnt, (10**9+7)))
