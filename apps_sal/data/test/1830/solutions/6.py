n,m=map(int,input().split())
xs=[0 for i in range(n)]
ys=[0 for i in range(n)]
l=0
k=0
for i in range(m):
    x,y=map(int,input().split())
    if xs[x-1]!=1:
        xs[x-1]=1
        l+=1
    if ys[y-1]!=1:
        ys[y-1]=1
        k+=1
    print(n*n-(l+k)*n+l*k,end=' ')

