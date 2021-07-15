for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    c.sort()
    if a==1:
        print(c[0]+b)
    else:
        if c[-1]-c[0]<=2*b:
            print(c[0]+b)
        else:
            print('-1')
