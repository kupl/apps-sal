from math import *

def dist(a,b,p):
	xu = b[0]-a[0]
	yu = b[1]-a[1]
	xv = p[0]-a[0]
	yv = p[1]-a[1]
	c1 = xu*xv + yu*yv
	c2 = xu*xu + yu*yu
	x,y = 0,0
	if c1<=0:
		x = a[0]-p[0]
		y = a[1]-p[1]
	elif c2<=c1:
		x = b[0]-p[0]
		y = b[1]-p[1]
	else:
		x = a[0] + xu*(c1/c2)-p[0]
		y = a[1] + yu*(c1/c2)-p[1]
	return x*x + y*y


n,cx,cy = map(int,input().split())
pts =  [ list(map(int,input().split())) for _ in range(n) ]
mini,maxi = float('inf'),0
for i in range(n):
	px,py = pts[i]
	maxi = max((px-cx)**2+(py-cy)**2,maxi)
	mini = min(dist(pts[i-1],pts[i],[cx,cy]),mini)
print((maxi-mini)*pi)
