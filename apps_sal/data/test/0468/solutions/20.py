import math
x,y = list(map(int, input().split()))
d1 = x*math.log(y)
d2 = y*math.log(x)
if(d1>d2):
	print("<")
elif(d2>d1):
	print(">")
else:
	print("=")
