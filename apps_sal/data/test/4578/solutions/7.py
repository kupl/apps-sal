N,X=list(map(int,input().split()))
l=[int(input()) for i in range(N)]
X-=sum(l)
ans=len(l)
ans+=X//min(l)
print(ans)
