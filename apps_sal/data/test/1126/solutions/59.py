n,x,m=map(int,input().split())
id=[-1]*(m+1)
s=[]
c=0
while(id[x]==-1):
    id[x]=c
    c+=1
    s.append(x)
    x=x*x%m
d=c-id[x]
ans=0
if d>=n:
    for i in range(n):
        ans+=s[i]
else:
    for i in range(id[x]):
        ans+=s[i]
    n-=id[x]
    sum=0
    for i in range(d):
        sum+=s[id[x]+i]
    ans+=(n//d)*sum
    n=n%d
    for i in range(n):
        ans+=s[id[x]+i]
print(int(ans))
