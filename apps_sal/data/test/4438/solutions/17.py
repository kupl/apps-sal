import sys
 
def minp():
	return sys.stdin.readline().strip()
 
def dist(a,b):
	return abs(a[1]-b[1])+abs(a[2]-b[2])
 
n = int(minp())
a = [None]*n
for i in range(n):
	x,y = list(map(int,minp().split()))
	a[i] = (max(x,y),x,-y)
a.sort()
#print(a)
d0 = 0
d1 = 0
p0 = (0,0,0)
p1 = (0,0,0)
i = 0
k = 1
while i < n:
	x = a[i]
	xx = x[0]
	j = i + 1
	while j < n and a[j][0] == xx:
		j += 1
	y = a[j-1]
	dd = dist(x,y)
	d2 = dist(p0,x)
	d3 = dist(p1,x)
	D0 = min(d0+d2,d1+d3)+dd
	P0 = y
	d2 = dist(p0,y)
	d3 = dist(p1,y)
	D1 = min(d0+d2,d1+d3)+dd
	P1 = x
	p0 = P0
	p1 = P1
	d0 = D0
	d1 = D1
	k += 1
	i = j
print(min(d0,d1))
	

