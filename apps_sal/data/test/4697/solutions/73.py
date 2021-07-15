n,m=map(int, input().split())
ans=0
if n>=m//2:
    ans=m//2
else:
    ans=n
    m-=n*2
    ans+=m//4
print(ans)
