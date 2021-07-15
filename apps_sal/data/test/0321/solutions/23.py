
import math as m
def f(a):
	if (a==2) : return True
	for i in range(2,round(m.sqrt(a))+1):
		if a%i==0:
			return False
	return True

t=int(input())


for i in range(t):
	a,b=input().split()

	a=int(a)
	b=int(b)

	if (a-b)==1 and f(a+b) :
		print("YES")
	else :
		print("NO")


