R=input
I=lambda:map(int,R().split())
n=int(R())
a=[]
b=[]
for i in range(n):x,y=I();a.append(x);b.append(y)
x=min(a)
y=max(b)
for i in range(n):
	if a[i]==x and b[i]==y:print(i+1);return
print(-1)
