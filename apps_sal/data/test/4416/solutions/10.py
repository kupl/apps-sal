import sys
import math
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return list(map(int, sys.stdin.readline().split()))

def SI():
	return sys.stdin.readline().strip()
n,k = MI()
x = []
y = []
z = []
o = []
for q in range(n):
	t,a,b = MI()
	if a == 1 and b == 1:
		z.append(t)
	elif a == 1:
		x.append(t)
	elif b == 1:
		y.append(t)
	else:
		o.append(t)
x.sort()
y.sort()
z.sort()
x0 = len(x)
y0 = len(y)
z0 = len(z)
if x0+z0<k or y0+z0<k:
	print(-1)
else:
	ans = 0
	l = r = 0
	for i in range(k):
		if l<x0 and l<y0 and r<z0:
			if x[l]+y[l]<z[r]:
				ans+=x[l]+y[l]
				l+=1
			else:
				ans+=z[r]
				r+=1
		elif r<z0:
			ans+=z[r]
			r+=1
		elif l<x0 and l<y0:
			ans+=x[l]+y[l]
			l+=1
	print(ans)

