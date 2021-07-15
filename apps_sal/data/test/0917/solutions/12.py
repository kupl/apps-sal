n,h,m=list(map(int,input().strip().split()))
buil=[h]*n
for i in range(m):
    l,r,x=list(map(int,input().strip().split()))
    for j in range(l-1,r):
        buil[j]=min(buil[j],x)
op=0
for i in buil:
    op+=i*i
print(op)
