n=int(input())
fa=[0,0]+list(map(int,input().split()))
delta=[0]*(n+1)
suml=[0]*(n+1)
for i in range(n,0,-1):
	if suml[i]==0:
		suml[i]=1
	delta[suml[i]]+=1
	suml[fa[i]]+=suml[i]

for i in range(1,n+1):
	delta[i]+=delta[i-1]
ans=0
for i in range(1,n+1):
	while delta[ans]<i:
		ans+=1
	print("%d "%ans,end="")
print("\n")
