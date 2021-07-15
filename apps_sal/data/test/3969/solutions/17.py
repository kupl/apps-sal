n,m=map(int,input().split())
l=[]
for i in range(n):
	a,b=input().split()
	l.append(int(a))
dp=[1]*n
for i in range(1,n):
	for j in range(0,i):
		if l[i]>=l[j]:	
			dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
