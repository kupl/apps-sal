import sys
input = sys.stdin.readline
def check(num):
	last = [0 for i in range(n)]
	for i in o:
		if i[0]>num:
			break
		else:
			last[i[1]-1] = i[0]
	b = [0 for i in range(num+1)]
	for i in range(n):
		b[last[i]] += a[i]

	i = 0
	c = 0
	d = 0
	for i in range(1,num+1):
		c += 1
		if(c >= b[i]):
			c -= b[i]
			b[i] = 0
		else:
			b[i] -= c
			c = 0

	s = sum(b)
	if s*2<=c:
		return True
	return False



n,m = map(int,input().split())
a = list(map(int,input().split()))
o = []
for i in range(m):
	x,y = map(int,input().split())
	o.append((x,y))
o.sort()
low = 1
high = sum(a)*2
while low<high:
	mid = (low+high)//2
	if check(mid):
		high = mid - 1
	else:
		low = mid + 1
if check(low):
	print (low)
else:
	print (low+1)
