n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=[0]*n
if a[0]>x:
    ans[0]=x
else:
    ans[0]=a[0]
for i in range(1,n):
    ans[i]=min(a[i],x-ans[i-1])
print(sum(a)-sum(ans))           
