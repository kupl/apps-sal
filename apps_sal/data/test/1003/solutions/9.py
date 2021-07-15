n,m=map(int,input().split())
ans=1
while n!=0:
    if ans%m==0:
        n+=1
    n-=1
    ans+=1
print(ans-1)
