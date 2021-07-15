n=int(input())
v1,v2=[],[]
for i in range(n):
	a,b=map(int,input().split(' '))
	v1.append(a)
	v2.append(b)
a,b=min(v1),max(v2)
t=0
for i in range(n):
	if(v1[i]<=a and v2[i]>=b):
		print(i+1)
		t=1
		break
if(t==0):
	print(-1)
