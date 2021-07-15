def dist2(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2
R,x1,y1,x2,y2 = list(map(int,input().split()))
if dist2(x1,y1,x2,y2) >= R**2:
    print(x1,y1,R)
else:
    d2 = dist2(x1,y1,x2,y2)
    if abs(d2)<0.0000000001:
        x = x1+R/2
        y = y1
        print(x,y,R/2)
    else:
        dd = d2**0.5+R
        dd /= 2
        x = x2+dd*(x1-x2)/(d2**0.5)
        y = y2+dd*(y1-y2)/(d2**0.5)
        print(x,y,dd)

