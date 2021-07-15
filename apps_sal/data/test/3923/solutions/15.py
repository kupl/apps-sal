n,a,b=map(int,input().split())
p=[i+1 for i in range(n)]
f=0
a,b=min(a,b),max(a,b)
for i in range(0,n+1,a):
	if (n-i)%b==0:
		x=((n-i)//b)
		f=1
		break
if f:
	for i in range(0,b*x,b):
		p[i:i+b]=[p[i+b-1]]+p[i:i+b-1]
	for j in range(b*x,n,a):
		p[j:j+a]=[p[j+a-1]]+p[j:j+a-1]
	print(*p)

else:
	print(-1)
