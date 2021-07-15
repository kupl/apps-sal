n,m=list(map(int,input().split()))
root=[[] for _ in range(n+1)]
for i in range(m):
    a,b=list(map(int,input().split()))
    root[a].append(b)
    root[b].append(a)
s=[0]*(n+1)
s[0]=1
s[1]=1
ans=0
def f(a,x):
    nonlocal ans
    for i in root[a]:
        if x[i]==0:
            x[i]=1
            f(i,x)
            x[i]=0
    if x.count(1)==n+1:
        ans+=1
f(1,s)
print(ans)


