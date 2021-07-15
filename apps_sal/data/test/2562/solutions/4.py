(input())
a=list(map(int,input().split()))
n,p=1000001,1000000007
cnt=[0]*n
curr=1
for i in a:
	cnt[i]+=1
ans=[0]*n
tot=0
for i in range(n-1,1,-1):
	k=sum(cnt[i::i])
	if k>0:
		ans[i]=(k*pow(2,k-1,p)-sum(ans[i::i]))%p
		tot=(tot+i*ans[i])%p
print(tot)


