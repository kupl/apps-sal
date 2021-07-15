import math
for _ in range(1):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    s=0
    d={0:1}
    for i in range(n):
        s+=a[i]
        if s in d:
            ans+=1
            s=a[i]
            d={0:1}
            d[s]=1
        else:
            d[s]=1
    print(ans)        
