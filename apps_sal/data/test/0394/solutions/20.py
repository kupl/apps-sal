n=int(input())
a=[0]
a+=list(map(int,input().split()))
x=[]
for i in range(1,n+1):
    x.append(a[i]-a[i-1])
ans=[]
b=a[1:]
for i in range(1,n+1):
    r=n%i
    c=x[:i]
    f=0
    if x[:r]!=x[n-r:]:
        continue
    for j in range(i,n-r,i):
        if x[j:j+i]!=c:
            f=1
    if f==0:
        ans.append(i)
print(len(ans))
print(*ans)

