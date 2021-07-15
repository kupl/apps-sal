n=int(input())
r=list(map(int,input().split()))
dp=[0]*(10**5+1)
cnt=[0]*(10**5+1)
tmp=[0]*(10**5+1)
mod=10**9+7
for i in range(n):
	cnt[r[i]]+=1
for i in range(1,10**5+1):
	for j in range(2*i,10**5+1,i):
		cnt[i]+=cnt[j]
	tmp[i]=pow(2,cnt[i],mod)-1
for i in range(10**5,0,-1):
	for j in range(2*i,10**5+1,i):
		tmp[i]=(tmp[i]-tmp[j])%mod
print(tmp[1]%mod)
