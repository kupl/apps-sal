n=int(input())
a=list(map(int,input().split()))
o=0
e=0
for i in range(n):
	if(a[i]%2==0):
		e+=1
	else:
		o+=1
if(o==n or e==n):
	print(*a)
else:
	a.sort()
	print(*a)
