n,m=list(map(int,input().split()))
s=[]
for i in range(n):
	p=input()
	for i in range(len(p)):
		if p[i]=='G':
			x=i
		elif p[i]=='S':
			y=i
	s.append([x,y])
ans=0
p=[]
for i in s:
	if i[0]>i[1]:
		print(-1)
		return
	elif i[0]<i[1]:
		p.append(i[1]-i[0])
t=0
p=set(p)
print(len(p)) 

