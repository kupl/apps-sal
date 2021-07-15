n,r=map(int,input().split())
l=list(map(int,input().split()))
c=[0]*n
ans=0
for i in range(n):
    if l[i]==1:
        b=False
        for j in range(i-(r-1),i+r):
            if j<0 or j>=n:
                continue
            if c[j]!=1:
                b=True
            c[j]=1

        if b:
            ans+=1

if c.count(0)==0:
    ans=1;i=0
    for j in range(r-1,-1,-1):
        if j>=n:
            continue
        if l[j]==1:
            i=j
            break
    while True:
        #print(i)
        if i+r-1>=n-1:
            break

        for j in range(i+2*(r-1)+1,i,-1):
            if j>=n:
                continue
            if l[j]==1:
                ans+=1
                i=j
                break

        if i+r-1>=n-1 or (i==n-1):
            break
    print(ans)

else:
    print(-1)
