n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(n):
    d=min(b[i],a[i]+a[i+1])
    c+=d
    a[i+1]-=max(0,d-a[i])
print(c)
