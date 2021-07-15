s=input()
pre=[0]
curr=-1
n=len(s)
for i in range(1,n):
	if s[i]=='v' and s[i-1]=='v':
		pre.append(pre[-1]+1)
	else:
		pre.append(pre[-1])
curr=0
ans=0
for i in range(n-2,-1,-1):
	if s[i]=='v' and s[i+1]=='v':
		curr+=1
	elif s[i]=='o':
		ans+=(curr)*(pre[i])
print(ans)

