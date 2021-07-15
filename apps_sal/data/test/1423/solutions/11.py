n, l, r = list(map(int, input().split()))
a = list(map(int, input().split()))
p = list(map(int, input().split()))
s = set()

x = []
for i in range(len(a)):
	x.append([p[i], i])

x.sort()
mx = -1000000000000
for i in range(n):
	p[x[i][1]] = max(l, mx + a[x[i][1]] + 1)
	if p[x[i][1]] > r:
		print('-1')
		return
	mx = p[x[i][1]] - a[x[i][1]]

idx = 0
for i in p:
	if idx != 0:
		print("", i, end="")
	else:
		print(i, end="")
		idx = 1
print('')

