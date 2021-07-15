n,m = input().split(' ')
n = int(n)
m = int(m)

av = []
bv = []

for i in range(m):
	t = input()
	a,b = t.split(' ')
	a = int(a)
	b = int(b)
	if a > b: a,b = b,a
	av.append(a)
	bv.append(b)

if m == 0:
	print(n-1)
	return

res = min(bv) - max(av)

if res <= 0 : res = 0
	
print(res)
