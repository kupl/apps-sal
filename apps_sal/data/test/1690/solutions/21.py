n=int(input())
a=list(map(int,input().split()))
summ=0
i=n-1
minn=a[i]
while i>=0:
    if minn>=a[i]:
        summ+=a[i]
        minn=a[i]-1
    else:
        summ+=minn
        minn=max(0,minn-1)
    i-=1
print(summ)
