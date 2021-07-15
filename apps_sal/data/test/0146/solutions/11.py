n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
s=0
for b in range(k):
	ans=0
	
	for i in range(1,n+1):
		if (i-b)%k!=0:
			ans+=a[i-1]
	s=max(s,abs(ans))
print(s)
