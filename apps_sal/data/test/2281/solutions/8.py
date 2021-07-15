#                                               |
#   _` |  __ \    _` |   __|   _ \   __ \    _` |   _` |
#  (   |  |   |  (   |  (     (   |  |   |  (   |  (   |
# \__,_| _|  _| \__,_| \___| \___/  _|  _| \__,_| \__,_|

import sys
import math

def read_line():
	return sys.stdin.readline()[:-1]
 
def read_int():
	return int(sys.stdin.readline())
	
def read_int_line():
	return [int(v) for v in sys.stdin.readline().split()]

def read_float_line():
	return [float(v) for v in sys.stdin.readline().split()]

n = read_int()
x1 = 0
y1 = n
ans = [0]*(2*n)

for i in range(1,n+1):
	if i&1:
		ans[x1] = i
		ans[x1+n-i] = i
		x1+=1
	else:
		ans[y1] = i
		ans[y1+n-i] = i
		y1+=1

for i in range(2*n):
	if ans[i] == 0:
		ans[i] = n

print(*ans)


