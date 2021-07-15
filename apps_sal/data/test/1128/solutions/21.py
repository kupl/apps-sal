ip=list(int(n) for n in input().split())
import math
a=ip[0]
m=ip[1]
a%=m
af=[a]
x=1;k=1;count=0;countlimit=int(math.floor(math.log(m,2)))
while (k==1):
	a=((a+a%m)%m)
	if a==0:
		print("Yes")
		k=0
	else:
		for check in af:
			if a==check:
				print("No")
				k=0
	if	count<=countlimit:
			af.append(a)
			count+=1
return

