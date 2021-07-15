n,k=list(map(int,input().split()))
s=list(map(int,input().split()))
x=sum(s[0:k])
ans=-1000000000000000
for i in range(n-k+1):
    av=sum(s[i:k+i])/k
    if av>ans:
        ans=av
    for j in range(n-k-i):
        av=(((av)*(k+j))+s[k+i+j])/(k+j+1)
        if av>ans:
            ans=av
print(ans)

