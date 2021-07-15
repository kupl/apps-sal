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

n,s = numIN()
a = list(numIN())
b = list(numIN())

if not a[0] or (a[s-1]==0 and b[s-1]==0):
	print('NO')
	return
if a[s-1]:
	print('YES')
	return
f = 0
for i in range(s,n):
	if a[i] and b[i]:
		f = 1
		break
if f:
	if b[s-1]:
		print('YES')
	else:
		print('NO')
else:
	print('NO')
