N=int(input())
cnt=[0 for _ in range(N+1)]
for i in range(1,N+1):
    cnt[i]=cnt[i-1]+1
    a=6
    while i-a>=0:
        cnt[i]=min(cnt[i],cnt[i-a]+1)
        a*=6
    a=9
    while i-a>=0:
        cnt[i]=min(cnt[i],cnt[i-a]+1)
        a*=9
print((cnt[N]))

