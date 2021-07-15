n,m,s,f=list(map(int,input().split()))
p=s
d=-1
c='L'
if s<f:
    d=1
    c='R'
t=1
ts={}
ans=""
for _ in range(m):
    x,y,z=list(map(int,input().split()))
    ts[x]=(y,z)
while(p!=f):
    if t in ts:
        (l,r)=ts[t]
        if l<=p<=r or l<=p+d<=r:
            ans+='X'
        else:
            p+=d
            ans+=c
    else:
        p+=d
        ans+=c
    t+=1
print(ans)

