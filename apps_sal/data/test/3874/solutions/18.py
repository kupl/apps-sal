n,m=list(map(int,input().split()))

a=[]
b=[]
for i in range(n):
	a.append(input())
	
t=list(map(int,input().split()))
flag=0
x=len(a[t[0]-1])
for i in t:
	b.append(a[i-1])
	if len(a[i-1])!=x:
		flag=1
		break

s=''
if flag!=1:
	for i in range(x):
		l=b[0][i]
		abc=0
		for j in range(m):
			if b[j][i]!=l:
				abc=1
				break
		if(abc==0):
			s+=l
		else:
			s+='?'
	
	
	for i in range(n):
		if i+1 not in t:
			if len(a[i])==x:
				flag=1
				for j in range(x):
					if(s[j]=='?'):
						pass
					elif(s[j]!=a[i][j]):
						flag=0
						break
		
		if flag==1:
			break
		
	if flag==1:
		print("No")
	
	else:
		print("Yes")
		print(s)

else:
	print("No")

