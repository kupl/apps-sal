n=int(input())
x=[]
y=[]
for i in range(n):
	s=input()
	s=s.split()
	x.append(int(s[0]))
	y.append(int(s[1]))
flag=0
for i in range(n):
	if(x[i]!=y[i]):
		flag=1
		break
	elif(i>0):
		if(x[i]>x[i-1]):
			flag=2
if(flag==1):
	print("rated")
elif(flag==2):
	print("unrated")
else:
	print("maybe")
	

