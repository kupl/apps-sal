for _ in range(1):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    k=0
    for i in range(n):
        if a[i]+b[i]!=2:
            if a[i]==1:
                ans+=1
            elif b[i]==1:
                k+=1
    if ans==0:
        print(-1)
    else:
        if k%ans==0:
            print(k//ans+1)
        else:
            print(k//ans+1)

