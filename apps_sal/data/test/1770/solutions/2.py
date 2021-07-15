from math import ceil
q = int(input())
for _ in range(q):
    n,x,y,d = list(map(int,input().split()))
    if (y-x)%d==0:
        print(abs(y-x)//d)
    elif (y-1)%d==0 and (n-y)%d==0:
        a = ceil((x-1)/d) + (y-1)//d
        b = ceil((n-x)/d) + (n-y)//d
        print(min(a,b))
    elif (y-1)%d==0:
        print(ceil((x-1)/d) + (y-1)//d)
    elif (n-y)%d==0:
        print(ceil((n-x)/d) + (n-y)//d)
    else:
        print(-1)

