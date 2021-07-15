n=int(input())
v=list(map(int, input().split()))
ans=0
for k in range(1,n):
	p,s=k,0
	while p<n:
		r=n-p-1
		if r<=k:
			break
		s+=v[p]+v[n-1-p]
		if r%k!=0 or p<r:
			ans=max(ans,s)
		p+=k
print(ans)
