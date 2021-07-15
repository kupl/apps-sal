n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
ans = [0] * n
for i in range(k):
	x, y = [int(j) - 1 for j in input().split()]
	if a[x] < a[y]:
		ans[y] -= 1
	if a[x] > a[y]:
		ans[x] -= 1
d = {}
e = {}
f = {}
for i in a:
	d[i] = 0
	f[i] = True
	e[i] = 0
for i in a:
	d[i] += 1
	e[i] += 1

wk1 = [i for i in a]
wk1.sort()
for i in range(n):
	if (f[wk1[i]]) and (wk1[i] != wk1[0]):
		d[wk1[i]] += d[wk1[i - 1]]
		f[wk1[i]] = False
for i in range(n):
	ans[i] += d[a[i]] - e[a[i]]

for i in range(n):
	if i != n - 1:
		print(ans[i], end = " ")
	else:
		print(ans[i])

