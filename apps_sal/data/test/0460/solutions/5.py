import math
p,x,y=map(int,input().split())
s=0
s=int(math.ceil((y-x)/50))
while(s<=1000000):
	score = x+50*s
	i=(score//50)%475
	l=[]

	for j in range(25):
		i=(i*96+42)%475
		l.append(26+i)
	if(p in l):
		break
	else:
		s+=1
if(s<=0):
	print(0)
else:
	print(int(math.ceil(s/2)))
