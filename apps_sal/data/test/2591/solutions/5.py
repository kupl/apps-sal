for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[0]*n
    i=n-1
    big=0
    foo=0
    while i>=0:
        if big==1:
            b[i]=a[-foo]
            big=0
        else:
            b[i]=a[foo]
            foo+=1
            big=1
        i-=1
    print(*b)
