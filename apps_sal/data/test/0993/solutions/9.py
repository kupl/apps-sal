n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
a[0]%=2
for i in range(n):
	a[i+1]+=a[i]
	a[i+1]%=m
a.sort()
ans=0
cnt=1
for i in range(n):
	if a[i]==a[i+1]:
		cnt+=1
	else:
		ans+=cnt*(cnt-1)//2
		cnt=1
ans+=cnt*(cnt-1)//2
print(ans)
