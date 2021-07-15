n,k=map(int,input().split())
d=[*map(int,input().split())]
cnt=[0]*k
for i in d:
    cnt[i%k]+=1
ans=cnt[0]//2
for i in range(1,k):
    req=k-i
    if i<req:
        ans+=min(cnt[i],cnt[req])
    elif i==req:
        ans+=cnt[i]//2
print(ans*2)
