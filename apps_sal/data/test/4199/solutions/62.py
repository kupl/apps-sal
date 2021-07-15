n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=sum(x>=k for x in l)
print(ans)
