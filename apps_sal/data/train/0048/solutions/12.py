for _ in range(int(input())):
	x,y,k=map(int,input().split()) 
	a=(y+1)*k-1 
	b=x-1 
	if a%b==0:
		c=a//b
	else:
		c=a//b+1 
	print(c+k)
