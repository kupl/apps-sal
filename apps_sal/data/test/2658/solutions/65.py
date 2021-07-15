n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(n+1)
count=0
now=1
f=1
for _ in range(k):
    if b[now]:
        f=0
        break
    count+=1
    b[now]=count
    now=a[now-1]
if f:
    print(now)
    return
x=count-b[now]+1
y=(k-b[now]+1)%x
for i in range(y):
    now=a[now-1]
print(now)
