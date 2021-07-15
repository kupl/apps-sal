n,x=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

add_a=[]
for i in range(n-1):
    add_a.append(max(a[i]+a[i+1]-x,0))

ans=0
for i in range(n-1):
    ans+=min(add_a[i],a[i+1])
    if i!=n-2:
        add_a[i+1]=max(0,add_a[i+1]-min(add_a[i],a[i+1]))
    add_a[i]-=min(add_a[i],a[i+1])
ans+=add_a[0]

print(ans)
