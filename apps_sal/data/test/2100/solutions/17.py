n=int(input())
l=r=0
for _ in range(n):
    x,y=map(int,input().split())
    l+=x
    r+=y
ans=min(n-l,l)
ans+=min(n-r,r)
print(ans)
