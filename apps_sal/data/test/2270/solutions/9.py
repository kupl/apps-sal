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
n = II()
a = LI()
d = [0]*(10**5+1)
t = 0
e = 0
for i in a:
	d[i]+=1
	if d[i]%4 == 0:
		t+=1
		e-=1
	elif d[i]%2 == 0:
		e+=1
for j in range(int(input())):
	q,i = input().split()
	i = int(i)
	if q == "+":
		d[i]+=1
		if d[i]%4 == 0:
			t+=1
			e-=1
		elif d[i]%2 == 0:
			e+=1
	else:
		d[i]-=1
		if d[i]%4 == 3:
			t-=1
			e+=1
		elif d[i]%4 == 1:
			e-=1
	boo = False
	if t > 1:
		boo = True
	elif t == 1 and e>1:
		boo = True
	print("YES" if boo else "NO")

