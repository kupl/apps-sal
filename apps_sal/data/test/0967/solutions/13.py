R=input
I=lambda:map(int,R().split())
n=int(R())
a=list(I())[::-1]+[999999]
for i in range(n):
	if a[i+1]>a[i]:print(n-i-1);break
