n, m = (int(x) for x in input().split())
a = []
for i in range(n):
	a.append(input())
ok = set('face')
ans = 0
for i in range(n - 1):
	for j in range(m - 1):
		test = set([a[i][j], a[i + 1][j], a[i][j + 1], a[i + 1][j + 1]])
		if test == ok:
			ans += 1
print(ans)

