from bisect import bisect_right as br
from bisect import bisect_left as bl
import sys
MAX = sys.maxsize
MAXN = 10**6+10
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a,b,x,y):
    return abs(a-x)+abs(b-y)

def numIN():
    return(map(int,sys.stdin.readline().strip().split()))

def charIN():
    return(sys.stdin.readline().strip().split())


def ans(a,l,n):
	f = 0
	cnt = 0
	for i in range(n):
		if a[i]>l:
			if not f:
				cnt+=1
				f = 1
		else:
			f = 0
	return cnt


n,m,l = numIN()
a = list(numIN())
cnt = ans(a,l,n)
fl = [0]*(n+1)
for i in range(n):
	if a[i]>l:
		fl[i]=1
for _ in range(m):
	x = list(numIN())
	if len(x)==1:
		print(cnt)
	else:
		p = x[1]-1
		d = x[2]
		a[p]+=d
		if a[p]>l:
			if not fl[p]:
				if p==0:
					if not fl[p+1]:
						cnt+=1
				elif p==n-1:
					if not fl[p-1]:
						cnt+=1
				else:
					if fl[p+1] and fl[p-1]:
						cnt-=1
					elif not (fl[p+1] or fl[p-1]):
						cnt+=1
			fl[p] = 1
