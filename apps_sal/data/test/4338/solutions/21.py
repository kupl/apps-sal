n,x,y=map(int,input().split())
a=list(map(int,input().split()))
ans=0
if y<x:
    print(n)
else:
    for i in range(n):
        if a[i]<=x:
            ans+=1
    print((ans+1)//2)
