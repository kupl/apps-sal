import math

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def mag(x,y):
    return math.sqrt(x**2 + y**2)

def main():
    PI = 3.141592653589793
    mags = []
    
    n, x0, y0 = map(int, input().split())

    x, y = x0, y0
    for i in range(n):
        x_, y_ = map(int, input().split())
        x_, y_ = x_ - x0, y_ - y0
        if i == 0:
            x1, y1 = x_ , y_
            x, y = x_, y_

        mags.append(mag(x_,y_))    

        if dot([x,y],[x-x_, y-y_])*dot([x_,y_],[x_-x,y_-y]) > 0:
            mags.append(abs(cross([x,y],[x_-x,y_-y])) / mag(x-x_,y-y_))
    
        x, y = x_, y_

    if dot([x,y],[x-x1,y-y1])*dot([x1,y1],[x1-x,y1-y]) > 0:
        mags.append(abs(cross([x,y],[x1-x,y1-y])) / mag(x-x1,y-y1))

    print((max(mags)**2 - min(mags)**2) * PI)

def __starting_point():
    main()
__starting_point()
