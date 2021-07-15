n,k=list(map(int,input().split()))
p=list(map(int,input().split()))
p.sort(reverse=False)
ans=0
for i in range(k):
    ans+=p[i]
print(ans)



