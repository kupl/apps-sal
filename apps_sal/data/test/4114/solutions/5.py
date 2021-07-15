n=int(input())

xl=[]
yl=[]
hl=[]



for i in range(n):
    xx,yy,hh=list(map(int,input().split()))
    xl.append(xx)
    yl.append(yy)
    hl.append(hh)

for cx in range(0,101):
    for cy in range(0,101):
        ok=True
        for i in range(n):
            x=xl[i]
            y=yl[i]
            h=hl[i]
            if h!=0:
                high = h + abs(x - cx) + abs(y - cy)
                break

        for i in range(n):
            x=xl[i]
            y=yl[i]
            h=hl[i]
            oh=max(high-abs(x-cx)-abs(y-cy),0)
            if h!=oh:
                ok=False
                break
        if ok:
            print(cx,cy,high)
            return
