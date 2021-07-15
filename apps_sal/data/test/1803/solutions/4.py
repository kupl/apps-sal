n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(0,m):
    x,y=list(map(int,input().split()))
    x=x-1
    if(x>0):
        a[x-1]+=y-1
    if(x<n-1):
        a[x+1]+=a[x]-y
    a[x]=0

for x in a:
    print (x)

