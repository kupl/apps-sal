n,c=map(int,input().split())
xv=[list(map(int,input().split())) for _ in range(n)]
l,r,lret,rret=[],[],[],[]
sl,sr=0,0
for i in range(n):
    sl+=xv[i][1]
    sr+=xv[n-i-1][1]
    l.append(sl-xv[i][0])
    lret.append(sl-2*xv[i][0])
    r.append(sr-(c-xv[n-i-1][0]))
    rret.append(sr-2*(c-xv[n-i-1][0]))
for i in range(1,n):
    lret[i]=max(lret[i],lret[i-1])
    rret[i]=max(rret[i],rret[i-1])
ans=max(0,max(l),max(r))
#print(l)
#print(r)
#print(lret)
#print(rret)
for i in range(n-1):
    ans=max(ans,l[i]+rret[n-i-2],r[i]+lret[n-i-2])
print(ans)
