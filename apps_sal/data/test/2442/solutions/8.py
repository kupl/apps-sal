import sys
import math
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return map(int, sys.stdin.readline().split())

def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
	n = II()
	a = LI()
	d = [0]*101
	for i in range(n):
		d[a[i]]+=1
	ans = 0
	boo = False
	for i in range(101):
		if boo == False and d[i]<2:
			ans+=i
			boo = True
		if boo == True and d[i]<1:
			ans+=i
			break
	print(ans)
