n=int(input())

l=1
r=n+1
for i in range(1,100):
	mid=(l+r)//2
	if n+1>=(n-mid+2)*(n-mid+1)//2:
		r=mid
	else:
		l=mid
print(r)
