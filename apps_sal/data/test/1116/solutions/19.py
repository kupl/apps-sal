t=int(input())
import math
for _ in range(t):
	a,b,k=map(int,input().split())
	if a<b:
		a,b=b,a
	if a==b:
		p=1
	elif a%b==0:
		p=a//b-1
	else:
		q=math.gcd(a,b)
		a//=q
		b//=q
		p=math.ceil((a-1)/b)
	if p>=k:
		print("REBEL")
	else:
		print("OBEY")
