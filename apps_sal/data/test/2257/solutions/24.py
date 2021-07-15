n,x,y,x1,y1=map(int,input().split())
a=[]
for i in range(n):
    xt,yt=map(int,input().split())
    a.append((((xt-x)**2+(yt-y)**2),((xt-x1)**2+(yt-y1)**2)))
a.sort(key=lambda x:x[0])
ans=max([x[1] for x in a])
ans=min(ans,a[-1][0])
r2=0
for i in range(n-2,-1,-1):
    r1=a[i][0]
    r2=max(r2,a[i+1][1])
    ans=min(ans,r1+r2)
print(ans)
