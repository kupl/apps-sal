N=int(input())
a=list(map(int,input().split()))
a.append(10**10)
a.sort()
n=0
c=0
ans=0
for i in range(N+1):
    if n!=a[i]:
        if n<c:ans+=c-n
        elif c<n:ans+=c
        n=a[i]
        c=1
    else:c+=1
print(ans)
