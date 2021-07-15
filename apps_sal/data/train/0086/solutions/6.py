for i in ' '*(int(input())):
    n=int(input())
    L=list(map(int,input().split()))
    s=sum(L)
    if s*2>n:
        if (n//2)%2:
            print(n//2+1)
            for i in ' '*(n//2+1):print(1,end=' ')
        else:
            print(n//2)
            for i in ' '*(n//2):print(1,end=' ')
    else:
        print(n//2)
        for i in ' '*(n//2):print(0,end=' ')
    print()
