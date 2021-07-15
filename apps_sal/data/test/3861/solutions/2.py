n = int(input())
a = list(map(int, input().split()))
a.sort()
import math
for i in a:
	if i < 0:
		r = i
	elif int(math.sqrt(i))**2 != i:
		r = i
print(r)
