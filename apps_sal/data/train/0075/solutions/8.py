import math

t=int(input())

while(t):
	t-=1
	n=int(input())

	ang= math.pi/(2*n)

	ans= 1/math.sin(ang)
	print(ans*math.cos(ang/2))
