from math import atan2
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x:atan2(x[1],x[0]))
ans=0
for i in range(n):
    x,y=0,0
    for j in range(n):
        x1,y1=l[(i+j)%n]
        x+=x1
        y+=y1
        ans=max(x**2+y**2,ans)
print(ans**0.5)
