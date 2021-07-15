a=list(map(int,input().split()))
n=a[0]
d=a[1]
s=0
gg=list(map(int,input().split()))
s=sum(gg)
if s+(n-1)*10>d:
	print('-1')
else:
	print((n-1)*2+(d-(s+(n-1)*10))//5 )

