3

n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
s = n * m
for i in range(n):
	black = sum(a[i])
	if black > 1:
		s += 2 ** black - black - 1
	white = m - black
	if white > 1:
		s += 2 ** white - white - 1

b = [[a[i][j] for i in range(n)] for j in range(m)]
for i in range(m):
	black = sum(b[i])
	if black > 1:
		s += 2 ** black - black - 1
	white = n - black
	if white > 1:
		s += 2 ** white - white - 1

print(s)
