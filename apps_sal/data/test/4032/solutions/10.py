n,k=map(int,input().split())
ar=list(map(int,input().split()))
i=0
for x in ar:
    if(x>k):
        break
    i+=1
ans=i
for x in ar[::-1]:
    if(x>k):
        break
    ans+=1

ans=min(n,ans)
print(ans)
