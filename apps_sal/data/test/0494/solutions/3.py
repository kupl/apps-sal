def f(a,b,c):
	if (a-b+c)%c==0:
		return c
	else:
		return (a-b+c)%c
n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
a=[0 for i in range(n)]
for i in range(m-1):
	if a[l[i]-1]==0 or a[l[i]-1]==f(l[i+1],l[i],n):
		a[l[i]-1]=f(l[i+1],l[i],n)
	else:
		print(-1)
		return
p=[i+1 for i in range(n)]
s=list(set(p)-set([i for i in a if i!=0]))
if len(s)!=a.count(0):
	print(-1)
	return
else:
	for i in range(n):
		if a[i]==0:
			a[i]=s[-1]
			s.pop()
for i in a:
	print(i,end=' ')
