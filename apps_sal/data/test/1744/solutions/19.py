n,m=list(map(int,input().split()))
if n==1:
	print(0)
	return
t=list(map(int,input().split()))
dp=[0]*101
ans=[]
for i in range(len(t)):
	s=0
	lim=m-t[i]
	f=False
	c=0
	for j in range(1,101):
		if f:
			c+=dp[j]
			continue
		if dp[j]:
			if s+dp[j]*j>lim:
				c+=dp[j]-(lim-s)//j
				f=True
			s+=dp[j]*j
	dp[t[i]]+=1
	ans.append(c)
print(*ans)

















