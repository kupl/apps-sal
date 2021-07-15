n, m = map(int, input().split())
d = {}
for i in range(n):
	im, num = input().split()
	d[num] = im
res = []
for j in range(m):
	im, num = input().split()
	res.append(im + ' ' + num + ' #' + d[num[:-1]])
for i in res:
	print(i)
