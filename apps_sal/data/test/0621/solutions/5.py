

import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

res = 0
v = []
p = 0
k = 0
for i in an:
	if(i < 0):
		if(p < 2):
			p += 1
		else:
			p = 1
			v.append(str(k))
			res += 1
			k = 0
	k += 1
	
if(k != 0):
	res += 1
	v.append(str(k))
	
print(res)
print(" ".join(v))

