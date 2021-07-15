import math
a,b,x = map(int,input().split())

if x >= (a**2) * b / 2 :
    theta = math.atan(2*(b-x/(a**2))/a)
    print(math.degrees(theta))
else :
    theta = math.pi/2-math.atan(2*x/((a*(b**2))))
    print(math.degrees(theta))
