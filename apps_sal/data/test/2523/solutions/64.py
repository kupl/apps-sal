S=list(input())
n=len(S)
ans=n
for _ in range(n-1):
	if S[_]!=S[_+1]:
		tmp=max(_+1,n-(_+1))
		ans=min(ans,tmp)

print(ans)

