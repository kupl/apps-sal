import math
a, b, x = map(int,input().split())
v1 = math.degrees(math.atan((a*b*b)/(2*x)))
v2 = math.degrees(math.atan((2*a*a*b-2*x)/(a*a*a)))
if a*a*b/2 > x:
    print('{:.7f}'.format(v1))
else:
    print('{:.7f}'.format(v2))
