n,x=map(int,input().split())
n=1<<n
ans=(n>>(x<n))-1
print(ans)
q,t=0,0
a=[0]*n
for i in range(1,n):
    if i<(i^x):
        a[t]=i^q
        q,t=i,t+1
print(*a[:t])
