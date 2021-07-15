def s():
    [x,y,n] = list(map(int,input().split()))
    res = (0,1)
    for b in range(1,n+1):
        a = int(round(b*x/y,0)+0.1)
        if abs(x*res[1]-y*res[0])*b > abs(x*b-y*(a-1))*res[1]:
            res = (a-1,b)
        if abs(x*res[1]-y*res[0])*b > abs(x*b-y*a)*res[1]:
            res = (a,b)
    print(*res,sep='/')
s()

