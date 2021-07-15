n=int(input())
a=list(map(int,input().split()))
l0=n+1
l1=n+1
for i in range(n):
	if a[i]==0:
		l0=i+1
	else:
		l1=i+1
print(min(l0,l1))
