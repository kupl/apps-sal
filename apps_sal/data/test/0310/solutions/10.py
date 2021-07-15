n,k=map(int,input().split())

ans=k//n
if(k%n):
    ans+=1
print(ans)
