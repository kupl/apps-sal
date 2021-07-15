import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n, m = mints()
	lines = []
	rows = [[0]*(m+2) for i in range(n)]
	col = [n]*(m+2)
	lstart = [[] for i in range(m+2)]
	lend = [[] for i in range(m+2)]
	dp = [[0]*(m+2) for i in range(m+2)]
	for i in range(n):
		for j in range(mint()):
			l, r = mints()
			lstart[l].append((i, r + 1))
			lend[r + 1].append((i, l))
	for i in range(1,m+2):
		for r, start in lend[i]:
			#print("end", r, start, i-1)
			for p in range(start, i):
				rows[r][p] -= 1
				if rows[r][p] == 0:
					col[p] += 1
		for r, end in lstart[i]:
			#print("start", r, i, end)
			for p in range(i, end):
				rows[r][p] += 1
				if rows[r][p] == 1:
					col[p] -= 1
		bcol = col.copy()
		brows = [rows[i].copy() for i in range(n)]
		#print(i, col)
		cc = [None]*(i-1)
		for j in range(i-1):
			for r, start in lend[j]:
				for p in range(start, j):
					rows[r][p] -= 1
					if rows[r][p] == 0:
						col[p] += 1
			for r, end in lstart[j]:
				for p in range(j, end):
					rows[r][p] += 1
					if rows[r][p] == 1:
						col[p] -= 1
			cc[j] = col.copy()

		for j in range(i-2,-1,-1):
			d = 0
			col = cc[j]
			for p in range(j+1, i):
				d = max(d, dp[j][p] + dp[p][i] + col[p]**2)
			dp[j][i] = d
			#print(j, i, col, d)
		col = bcol
		rows = brows
	print(dp[0][m+1])

solve()

