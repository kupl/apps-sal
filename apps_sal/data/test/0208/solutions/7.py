m=(list(int(x) for x in input().split()))
x1=m[0]
y1=m[1]
x2=m[2]
y2=m[3]

dx=abs(x1-x2)
dy=abs(y1-y2)

if not dx:
    y3=y1
    y4=y2
    x3=x1+dy
    x4=x2+dy    
    print(x3,y3,x4,y4)
elif not dy:
    x3=x1
    x4=x2
    y3=y1+dx
    y4=y2+dx
    print(x3,y3,x4,y4)
else:
    if dx==dy:
        x3=x1
        y3=y2
        x4=x2
        y4=y1
        print(x3,y3,x4,y4)  
    else:
        print("-1")
