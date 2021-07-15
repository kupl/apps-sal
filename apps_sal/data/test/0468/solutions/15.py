from math import log
a,b=[int(i) for i in input().split()]
x = log(a)
y = log(b)
if b *x == a* y:
	print("=")
elif x*b < a * y:
	print("<")
else :
	print(">")		
