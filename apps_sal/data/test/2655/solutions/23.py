n=int(input())
a=sorted(list(map(int, input().split())), reverse=True)
cur=1
cnt=0
ans=a[0]
for i in range(1, n-1):
    ans+=a[cur]
    cnt+=1
    if cnt==2:
        cur+=1
        cnt=0
print(ans)
