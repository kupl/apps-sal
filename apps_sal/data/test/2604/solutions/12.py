# your code goes here
import math
arr = input().split()
r = int(arr[0])
d = int(arr[1])

n = int(input())
ctr = 0
for i in range(n):
	arr = input().split()
	x = int(arr[0])
	y = int(arr[1])
	z = int(arr[2])
	
	x = abs(x)
	y = abs(y)
	
	l = math.sqrt(x*x + y*y)
	l -= z
	m = l + z + z
	if l >= r-d and m <= r:
		ctr += 1
print(str(ctr))
