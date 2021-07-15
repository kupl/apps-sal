import sys
from bisect import *
import math

N,X,K = list(map(int, input().split()))
p = sorted(list(map(int, input().split())))

def get(l, r):
	return (r//X) - (l-1)//X

p = sorted(p)
mp = {}
n = len(p)

for i in range(n):
	if p[i] in mp:
		continue
	else:
		mp[p[i]] = i
x = 5
ans = 0
mx = 0

for i in range(0,n):
	x = p[i]
	a = x//X
	mn = 0
	mx = 0

	if x % X == 0 :
		mn = x + (K-1)*X
		mx = mn + X-1
	else:
		mn =(x//X)*X + (K)*X
		mx = mn + X-1
	if K == 0:
		if x%X == 0 :
			continue
		mn = x
		mx = (x//X)*X+X-1
	#print(x,mn,mx)
	if mn > mx:
		continue
	ans = ans + bisect_right(p,mx) - bisect_left(p,mn)

print(ans)

