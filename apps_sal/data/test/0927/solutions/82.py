n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
p=[2,5,5,4,5,6,3,7,6]
num=[]
for x in a:
	num.append(p[x-1])
inf=10**8
dp=[-inf]*(n+1)
dp[0]=0
for i in range(n):
	for j in range(m):
		if i+num[j]<=n and dp[i]!=-inf:
			dp[i+num[j]]=max(dp[i+num[j]],dp[i]+1)
ans=""
now=n
for i in range(dp[n]):
	for j in range(m-1,-1,-1):
		if now-num[j]<0:
			continue
		if dp[now-num[j]]==dp[now]-1:
			now-=num[j]
			ans+=str(a[j])
			break
print(ans)
