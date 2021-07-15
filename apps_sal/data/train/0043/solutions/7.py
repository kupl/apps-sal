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
t = II()
for q in range(t):
	n = II()
	a = LI()
	b = LI()
	b = sorted(enumerate(b), key=lambda x: a[x[0]])
	b = [i[1] for i in b]
	a.sort()
	x = []
	s = 0
	for i in range(n-1,-1,-1):
		s+=b[i]
		x.append(s)
	x = x[:][::-1]
	ans = s
	for i in range(n):
		if i == n-1:
			ans = min(ans,a[i])
		else:
			ans = min(ans,max(a[i],x[i+1]))
	print(ans)

