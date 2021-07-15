N=int(input())
a=list(map(int,input().split()))
a.sort()
a.append(0)
i=0
ans=0
while i<N:
    x=a[i]
    count=0
    while a[i]==x:
        i+=1
        count+=1
    if count<x:
        ans+=count
    else:
        ans+=count-x
print(ans)

