A,B=map(int,input().split())
cnt=1
ans=0
while cnt<B:
    cnt+=A-1
    ans+=1
print(ans)
