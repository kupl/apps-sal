x,y=list(map(int,input().split()))
s=input()
t=input()
l=[i for i in range(1,x+1)]
ans=x
for i in range(1+y-x):
	temp=0
	k=[]
	for j in range(x):
		if s[j:j+1]!=t[i+j:i+j+1]:
			temp+=1
			k.append(j+1)
	if temp<ans:
		ans=temp
		l=k
print (ans)
print(*l)

