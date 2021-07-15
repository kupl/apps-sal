'''input
8
1 4
487 1
487 2
487 3
487 4
487 5
487 6
487 7
'''
import math
def dig(x):
	mn = x%10
	mx = x%10
	while x>0:
		mn = min(mn,x%10)
		mx = max(mx,x%10)
		x//=10
	return mn,mx
def solve():
	a,k = map(int,input().split())
	l = [a]
	ln = 1
	for i in range(1000):
		pv = l[ln-1]
		mn,mx = dig(pv) 
		if mn ==0:
			break
		l.append(pv+mx*mn)
		ln+=1
	k = min(k,len(l))
	print(l[k-1])
	return
t = 1
t = int(input())
while t>0:
	t-=1
	solve()
