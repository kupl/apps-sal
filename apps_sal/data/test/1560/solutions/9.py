from math import ceil

n=int(input())
col=list(input())

nr=col.count('r')
nb=col.count('b')

dif=int(abs(nr-nb)/2)

c1=0
c2=0

for i in range(len(col)):
	if i%2==0:
		if col[i]=='b':
			c1+=1
		else:
			c2+=1
	else:
		if col[i]=='r':
			c1+=1
		else:
			c2+=1

c=min(c1,c2)

print(int(ceil((c-dif)/2))+dif)
