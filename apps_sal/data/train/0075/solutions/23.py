import math
q = int(input())
for _ in range(q):
	n = int(input())
	alfa = 3*math.pi/4 - ((n//2)*math.pi/(2*n))
	y = math.tan(math.pi/2-math.pi/(2*n))
	x = y/math.cos(math.pi/(2*n))
	bok = math.sin(alfa)*x
	print(bok)
