for i in range(int(input())):
    n,x,y,d=map(int,input().split())
    if y==1 or y==n:
        print(abs(-abs(x-y)//d))
    elif abs(x-y)%d==0:
        print(abs(x-y)//d)
    elif abs(1-y)%d==0 and abs(n-y)%d==0:
        print(min(abs(-abs(x-1)//d)+(y-1)//d,abs(-abs(x-n)//d)+(n-y)//d))
    elif abs(1-y)%d==0:
        print(abs(-abs(x-1)//d)+(y-1)//d)
    elif abs(n-y)%d==0:
        print(abs(-abs(x-n)//d)+(n-y)//d)
    else:
        print(-1)
