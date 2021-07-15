n = int(input())
a = []
for _ in range(n):
	l, r = list(map(int, input().split()))
	a.append([l, r])

m = int(input())
b = []
for _ in range(m):
	l, r = list(map(int, input().split()))
	b.append([l, r])

b.sort()
res = 0
for i in a:
	res = max(b[m - 1][0] - i[1], res)

a.sort()
for i in b:
	res = max(a[n - 1][0] - i[1], res)
	
print(res)

