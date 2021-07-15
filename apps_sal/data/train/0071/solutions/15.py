for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    av = 0
    for i in range(n):
        if a[i]<0:
            cr = min(-1*a[i],av)
            a[i]+=cr
            av-=cr
            cnt+=a[i]
            a[i]=0
        else:
            av+=a[i]
    print(-1*cnt)
