import math
q = int(input())
for _ in range(q):
	n = int(input())
	n*=2
	print(math.tan(math.pi/2-math.pi/n))
