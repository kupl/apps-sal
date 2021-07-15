n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
maxx,minn=0,0
if a[0]>b[1]:
    maxx+=(a[0]-b[1])
if a[1]>b[2]:
    maxx+=(a[1]-b[2])
if a[2]>b[0]:
    maxx+=(a[2]-b[0])
if a[0]>b[0]+b[2]:
    minn+=(a[0]-b[0]-b[2])
if a[1]>b[1]+b[0]:
    minn+=(a[1]-b[1]-b[0])
if a[2]>b[1]+b[2]:
    minn+=(a[2]-b[1]-b[2])
print(minn,n-maxx)
