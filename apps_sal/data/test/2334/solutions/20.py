import math
n=input()
a=list(map(int,input().split()))
x,f=list(map(int,input().split()))
ans=0
for i in a:
	if i>x:
		ans+= math.ceil((i-x)/(x+f))

print((ans)*f)

