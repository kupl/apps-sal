from math import *
from sys import stdin, stdout 

io = stdin.readline().split()

w = float(io[0])
h = float(io[1])
a = float(io[2])

if (a > 90): a = 180 - a

if (a == 0) :
    print(w * h)
elif (a == 90) :
    print(min(w, h) ** 2)
else :
    a = a * pi / 180.0
    if (w < h) : w, h = h, w
    corner_x = cos(a) * (w / 2.0) + sin(a) * (h / 2.0)
    if (corner_x >= w / 2 ) :
        x0 = w / 2.0 + (h / 2.0 - (h / 2.0) / cos(a)) * (cos(a) / sin(a))
        y0 = h / 2.0 - (tan(a) * (- w / 2.0) + (h / 2.0) / cos(a))
        x1 = w / 2.0 - (h / 2.0 - (w / 2.0) / sin(a)) * (-tan(a))
        y1 = h / 2.0 - ((-cos(a) / sin(a)) * (w / 2.0) + (w / 2.0) / sin(a))

        print(w * h - x1 * y1 - x0 * y0)
    else :
        y = tan(a) * (w / 2.0) - (h / 2.0) / cos(a) + h / 2.0
        y0 = y - h
        x0 = y * tan(pi / 2.0 - a)
        print(w * h - (y0 * tan(pi / 2.0 - a) + x0) * h)
    



