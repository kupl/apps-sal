n=int(input())
*a,=map(int,input().split())
l=[abs(a[i]-a[i-1]) for i in range(1,n)]
ans=0
x=y=0
for i in range(n-1):
    t=[l[i],-l[i]][i%2]
    x+=t
    y-=t
    ans=max(ans,x,y)
    x=max(x,0)
    y=max(y,0)
print(ans)
