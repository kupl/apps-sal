N=int(input())
a=list(map(int,input().split()))
ans=10000000000000000000
c=0
s=sum(a)
for i in range(N-1):
    c+=a[i]
    s-=a[i]
    if abs(c-s)<ans:
        ans=abs(c-s)
print(ans)

