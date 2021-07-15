U=1
D=-1
x,y=map(int,input().split())
k=A=B=0
while 1:
	a,b=U,B;k+=1
	if (A<=x<=a or a<=x<=A)and(B<=y<=b or b<=y<=B):break
	A=a;b=U;k+=1
	if (A<=x<=a or a<=x<=A)and(B<=y<=b or b<=y<=B):break
	B=b;a=D;k+=1
	if (A<=x<=a or a<=x<=A)and(B<=y<=b or b<=y<=B):break
	A=a;b=D;k+=1
	if (A<=x<=a or a<=x<=A)and(B<=y<=b or b<=y<=B):break
	A,B=a,b
	U+=1;D-=1
if k<1:k=1
print(k-1)
