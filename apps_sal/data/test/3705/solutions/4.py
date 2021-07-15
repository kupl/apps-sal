n=int(input())
r=input()
c=0
for i in r:
	if i=='8':
		c=c+1
print (min(n//11,c))
