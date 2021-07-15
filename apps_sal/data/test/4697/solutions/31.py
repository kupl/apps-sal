n,m=list(map(int,input().split()))
if n*2>=m:
    ans=m//2
else:
    ans=n
    m-=n*2
    ans+=m//4
print(ans)

