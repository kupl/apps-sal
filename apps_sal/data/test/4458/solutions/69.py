n=int(input())
p=list(map(int,input().split()))
ans=0
m=2*10**5+1
for i in range(n):
    if m>p[i]:
        m=p[i]
        ans+=1
print(ans)
