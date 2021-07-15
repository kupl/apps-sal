R=lambda:list(map(int,input().split()))
n,m=R()
A=[]
while(n>0):
	n-=1
	c,t=R()
	A.append(c*t)
i=p=0
for v in R():
	while(p<v):
		p+=A[i]
		i+=1
	print(i)

