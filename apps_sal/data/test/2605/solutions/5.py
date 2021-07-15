n,k=input().split()
n,k=int(n),int(k)
beaut=[]
ans=0
sum=0
cap=[0 for i in range(n)]
beaut=[int(i) for i in input().split()]
v=[int(i) for i in input().split()]
for i in range(n):
	sum=sum+beaut[i]
for i in range(k):
	cap[v[i]-1]=1

for i in range(n):
	if(cap[i]==1):
		sum=sum-beaut[i]
		ans=ans+beaut[i]*sum

for i in range(n):
	if(cap[i]==0):
		if(cap[(i+1)%n]==0):
			ans=ans+beaut[i]*beaut[(i+1)%n]
print(ans)
