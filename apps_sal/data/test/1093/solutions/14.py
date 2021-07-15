n, m = map(int, input().split())
arr = [list(map(str, input())) for i in range(n)]
ans = [0] * m
for i in range(n):
	for j in range(m):
		if (arr[i][j] == '*'):
			ans[j] += 1
pos = ans[0]
up = 0
dn = 0
for i in range(1, m):
	npos = ans[i]
	if (npos < pos):
		dn = max(dn, pos - npos)
	else:
		up = max(up, npos - pos)
	pos = npos
print(up, dn)
